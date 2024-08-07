from pathlib import Path
from omegaconf import DictConfig
import numpy as np
import time
from tqdm import tqdm
import random
import math
from copy import deepcopy
from datetime import datetime
import platform
import cv2

import torch
import torch.nn as nn
from torch.optim import lr_scheduler
import torch.distributed as dist

from ycsai.utils import RANK, LOGGER, TQDM_BAR_FORMAT, GIT_INFO
from ycsai.utils.torch_utils import (
    _init_ddp, _init_seeds, 
    select_device, torch_distributed_zero_first,
    smart_optimizer, ModelEMA, smart_DDP,
    de_parallel, EarlyStopping
)
from ycsai.utils.general import (
    increment_path, yaml_save, check_dataset,
    check_suffix, intersect_dicts, check_amp,
    check_img_size, one_cycle, one_flat_cycle,
    labels_to_class_weights, fitness,
    strip_optimizer, Profile, non_max_suppression,
    scale_boxes, xyxy2xywh
)
from ycsai.utils.download import(
    attempt_download_asset
)
from ycsai.utils.loss import ComputeLoss
from ycsai.utils.experiments import attempt_load
import ycsai.utils.val as validate
from ycsai.utils.plots import Annotator

from ycsai.models.tasks import Model
from ycsai.data.dataloader import (
    create_dataloader, LoadImages, IMG_FORMATS, VID_FORMATS
)
from ycsai.layers.modules import DetectMultiBackend


class Engine:
    def __init__(self, cfg: DictConfig):
        """ Initialize model """
        super().__init__()        
        if cfg.model.task == 'predict':
            print("predict")
            self.set_device = select_device(cfg.predict.device)
            # Run predict
            self.do_detect(cfg)
        elif cfg.model.task == 'train':
            # Set device
            self.set_device = select_device(cfg.model.device, cfg.model.batch)
            if self.set_device.type in {"cpu"}:
                pass
            elif RANK != -1:
                self.set_device, self.world_size = _init_ddp(cfg.model.device)
            else:
                self.world_size = 1
            _init_seeds(cfg.model.seed + 1 + RANK, deterministic=cfg.model.deterministic)
            # Save Directories
            if RANK in {-1, 0}:
                self.save_dir = str(increment_path(Path(cfg.model.project) / cfg.model.folder, exist_ok=False))
                LOGGER.info('save experiments: '+ self.save_dir)
                self.save_dir = Path(self.save_dir)
                self.w = self.save_dir / 'weights'  # weights dir
                self.w.mkdir(parents=True, exist_ok=True)  # make dir
                self.last, self.best = self.w / 'last.pt', self.w / 'best.pt'
                self.last_striped, self.best_striped = self.w / 'last_striped.pt', self.w / 'best_striped.pt'
                # Hyperparameters
                LOGGER.info('hyperparameters: ' + ', '.join(f'{k}={v}' for k, v in cfg.hyp.items()))
                yaml_save(self.save_dir / 'hyp.yaml', cfg.hyp)
            # Set dataset
            self.data_dict = None
            with torch_distributed_zero_first(RANK):  # avoid auto-downloading dataset multiple times
                self.data_dict = check_dataset(cfg.model.data)
            self.train_path, self.val_path = self.data_dict['train'], self.data_dict['val']
            self.nc = int(self.data_dict['nc'])  # number of classes
            self.names = self.data_dict['names']  # class names
            # Set model
            self.model = self.set_model(cfg)
            # Run train
            self.do_train(cfg)
    
    def set_model(self, cfg: DictConfig):
        check_suffix(cfg.model.weights, '.pt')  # check weights
        pretrained = cfg.model.weights.endswith('.pt')
        if pretrained:
            with torch_distributed_zero_first(RANK):
                weights = attempt_download_asset(cfg.model.weights)  # download if not found locally
            ckpt = torch.load(weights, map_location='cpu')  # load checkpoint to CPU to avoid CUDA memory leak
            # print(self.set_device)
            model = Model(cfg.model.name or ckpt['model'].yaml, ch=3, nc=self.nc, anchors=cfg.hyp.get('anchors')).to(self.set_device)  # create
            exclude = ['anchor'] if (cfg.model.name or cfg.hyp.get('anchors')) else []  # exclude keys
            csd = ckpt['model'].float().state_dict()  # checkpoint state_dict as FP32
            csd = intersect_dicts(csd, model.state_dict(), exclude=exclude)  # intersect
            model.load_state_dict(csd, strict=False)  # load
            if RANK in {-1, 0}:
                LOGGER.info(f'run Transferred {len(csd)}/{len(model.state_dict())} items from {weights}')  # report
            return model
        else:
            model = Model(cfg.model.name, ch=3, nc=self.nc, anchors=cfg.hyp.get('anchors')).to(self.set_device)  # create
            return model
    
    def do_train(self, cfg: DictConfig):
        amp = check_amp(self.model)  # check AMP

        # Freeze
        freeze = [f'model.{x}.' for x in (cfg.model.freeze if len(cfg.model.freeze) > 1 else range(cfg.model.freeze[0]))]  # layers to freeze
        for k, v in self.model.named_parameters():
            # v.requires_grad = True  # train all layers TODO: uncomment this line as in master
            # v.register_hook(lambda x: torch.nan_to_num(x))  # NaN to 0 (commented for erratic training results)
            if any(x in k for x in freeze):
                LOGGER.info(f'freezing {k}')
                v.requires_grad = False
        
        # Image size
        gs = max(int(self.model.stride.max()), 32)  # grid size (max stride)
        imgsz = check_img_size(cfg.model.imgsz, gs, floor=gs * 2)  # verify imgsz is gs-multiple (32*imgsz)

        # Optimizer
        nbs = 64  # nominal batch size
        accumulate = max(round(nbs / cfg.model.batch), 1)  # accumulate loss before optimizing
        cfg.hyp.weight_decay *= cfg.model.batch * accumulate / nbs  # scale weight_decay
        optimizer = smart_optimizer(self.model, cfg.model.optim, cfg.hyp.lr0, cfg.hyp.momentum, cfg.hyp.weight_decay)

        # Scheduler
        if cfg.model.cos_lr:
            lf = one_cycle(1, cfg.hyp.lrf, cfg.model.epochs)  # cosine 1-cfg.hyp.lrf
        elif cfg.model.flat_cos_lr:
            lf = one_flat_cycle(1, cfg.hyp.lrf, cfg.model.epochs)  # flat cosine 1->cfg.hyp.lrf       
        elif cfg.model.fixed_lr:
            lf = lambda x: 1.0
        else:
            lf = lambda x: (1 - x / cfg.model.epochs) * (1.0 - cfg.hyp.lrf) + cfg.hyp.lrf  # linear

        scheduler = lr_scheduler.LambdaLR(optimizer, lr_lambda=lf)
        # from utils.plots import plot_lr_scheduler; plot_lr_scheduler(optimizer, scheduler, epochs)

        # EMA
        ema = ModelEMA(self.model) if RANK in {-1, 0} else None

        # DP mode
        if RANK == -1 and torch.cuda.device_count() > 1:
            LOGGER.warning('DP not recommended, use torch.distributed.run for best DDP Multi-GPU results.')
            self.model = torch.nn.DataParallel(self.model)

        # SyncBatchNorm
        if cfg.model.sync_bn and RANK != -1:
            self.model = torch.nn.SyncBatchNorm.convert_sync_batchnorm(self.model).to(self.set_device)
            LOGGER.info('Using SyncBatchNorm()')
        
        # Dataset loader
        train_loader, dataset = create_dataloader(self.train_path,
                                                imgsz,
                                                cfg.model.batch // self.world_size,
                                                gs,
                                                hyp=cfg.hyp,
                                                augment=True,
                                                cache=None if cfg.model.cache == 'val' else cfg.model.cache,
                                                rank=RANK,
                                                workers=cfg.model.workers,
                                                close_mosaic=cfg.model.close_mosaic != 0,
                                                prefix='Train dataset: ',
                                                shuffle=True,
                                                min_items=0)
        labels = np.concatenate(dataset.labels, 0)
        mlc = int(labels[:, 0].max())  # max label class
        assert mlc < self.nc, f'Label class {mlc} exceeds nc={self.nc} in {cfg.model.data}. Possible class labels are 0-{self.nc - 1}'

        if RANK in {-1, 0}:
            val_loader = create_dataloader(self.val_path,
                                        imgsz,
                                        cfg.model.batch // self.world_size * 2,
                                        gs,
                                        hyp=cfg.hyp,
                                        cache=None if cfg.model.cache == 'novalid' else cfg.model.cache,
                                        rect=True,
                                        rank=-1,
                                        workers=cfg.model.workers * 2,
                                        pad=0.5,
                                        prefix='val: ')[0]
        # DDP mode
        if RANK != -1:
            self.model = smart_DDP(self.model)
        
        # Model attributes
        nl = de_parallel(self.model).model[-1].nl  # number of detection layers (to scale hyps)
        self.model.nc = self.nc  # attach number of classes to model
        self.model.hyp = cfg.hyp  # attach hyperparameters to model
        self.model.class_weights = labels_to_class_weights(dataset.labels, self.nc).to(self.set_device) * self.nc  # attach class weights
        self.model.names = self.names

        # Start training
        start_epoch, best_fitness = 0, 0.0
        t0 = time.time()
        nb = len(train_loader)  # number of batches
        nw = max(round(cfg.hyp.warmup_epochs * nb), 100)  # number of warmup iterations, max(3 epochs, 100 iterations)
        # nw = min(nw, (epochs - start_epoch) / 2 * nb)  # limit warmup to < 1/2 of training
        last_opt_step = -1
        maps = np.zeros(self.nc)  # mAP per class
        results = (0, 0, 0, 0, 0, 0, 0)  # P, R, mAP@.5, mAP@.5-.95, val_loss(box, obj, cls)
        scheduler.last_epoch = start_epoch - 1  # do not move
        scaler = torch.cuda.amp.GradScaler(enabled=amp)
        stopper, stop = EarlyStopping(patience=cfg.model.patience), False
        compute_loss = ComputeLoss(self.model)  # init loss class
        if RANK in {-1, 0}:
            LOGGER.info(f'Image sizes {imgsz} train, {imgsz} val\n'
                        f'Using {train_loader.num_workers * self.world_size} dataloader workers\n'
                        f'Starting training for {cfg.model.epochs} epochs...')
        # epochs
        for epoch in range(start_epoch, cfg.model.epochs):
            self.model.train()
            
            if epoch == (cfg.model.epochs - cfg.model.close_mosaic):
                LOGGER.info("Closing dataloader mosaic")
                dataset.mosaic = False
            
            mloss = torch.zeros(3, device=self.set_device)  # mean losses
            if RANK != -1:
                train_loader.sampler.set_epoch(epoch)
            pbar = enumerate(train_loader)
            if RANK in {-1, 0}:
                LOGGER.info(('\n' + '%11s' * 7) % ('Epoch', 'GPU_mem', 'box_loss', 'cls_loss', 'dfl_loss', 'Instances', 'Size'))
                pbar = tqdm(pbar, total=nb, bar_format=TQDM_BAR_FORMAT)  # progress bar
            optimizer.zero_grad()

            # batches
            for i, (imgs, targets, paths, _) in pbar:
                ni = i + nb * epoch # number integrated batches
                imgs = imgs.to(self.set_device, non_blocking=True).float() / 255  # uint8 to float32, 0-255 to 0.0-1.0
                # Warmup
                if ni <= nw:
                    xi = [0, nw]  # x interp
                    # compute_loss.gr = np.interp(ni, xi, [0.0, 1.0])  # iou loss ratio (obj_loss = 1.0 or iou)
                    accumulate = max(1, np.interp(ni, xi, [1, nbs / cfg.model.batch]).round())
                    for j, x in enumerate(optimizer.param_groups):
                        # bias lr falls from 0.1 to lr0, all other lrs rise from 0.0 to lr0
                        x['lr'] = np.interp(ni, xi, [cfg.hyp.warmup_bias_lr if j == 0 else 0.0, x['initial_lr'] * lf(epoch)])
                        if 'momentum' in x:
                            x['momentum'] = np.interp(ni, xi, [cfg.hyp.warmup_momentum, cfg.hyp.momentum])
                # Multi-scale
                if cfg.model.multi_scale:
                    sz = random.randrange(imgsz * 0.5, imgsz * 1.5 + gs) // gs * gs  # size
                    sf = sz / max(imgs.shape[2:])  # scale factor
                    if sf != 1:
                        ns = [math.ceil(x * sf / gs) * gs for x in imgs.shape[2:]]  # new shape (stretched to gs-multiple)
                        imgs = nn.functional.interpolate(imgs, size=ns, mode='bilinear', align_corners=False)
                # Forward
                with torch.cuda.amp.autocast(amp):
                    pred = self.model(imgs)  # forward
                    loss, loss_items = compute_loss(pred, targets.to(self.set_device))  # loss scaled by batch_size
                    if RANK != -1:
                        loss *= self.world_size  # gradient averaged between devices in DDP mode
                # Backward
                scaler.scale(loss).backward()
                # Optimize - https://pytorch.org/docs/master/notes/amp_examples.html
                if ni - last_opt_step >= accumulate:
                    scaler.unscale_(optimizer)  # unscale gradients
                    torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=10.0)  # clip gradients
                    scaler.step(optimizer)  # optimizer.step
                    scaler.update()
                    optimizer.zero_grad()
                    if ema:
                        ema.update(self.model)
                    last_opt_step = ni
                # Print
                if RANK in {-1, 0}:
                    mloss = (mloss * i + loss_items) / (i + 1)  # update mean losses
                    mem = f'{torch.cuda.memory_reserved() / 1E9 if torch.cuda.is_available() else 0:.3g}G'  # (GB)
                    pbar.set_description(('%11s' * 2 + '%11.4g' * 5) %
                                        (f'{epoch}/{cfg.model.epochs - 1}', mem, *mloss, targets.shape[0], imgs.shape[-1]))
            # end batches

            # Scheduler
            lr = [x['lr'] for x in optimizer.param_groups]  # for loggers
            scheduler.step()
            # mAP
            if RANK in {-1, 0}:
                ema.update_attr(self.model, include=['yaml', 'nc', 'hyp', 'names', 'stride', 'class_weights'])
                final_epoch = (epoch + 1 == cfg.model.epochs) or stopper.possible_stop
                noval = cfg.model.cache == 'novalid'
                if not noval or final_epoch:  # Calculate mAP
                    results, maps, _ = validate.run(self.data_dict,
                                                    batch_size=cfg.model.batch // self.world_size * 2,
                                                    imgsz=imgsz,
                                                    half=amp,
                                                    model=ema.ema,
                                                    dataloader=val_loader,
                                                    save_dir=self.save_dir,
                                                    plots=False,
                                                    compute_loss=compute_loss)
                # Update best mAP
                fi = fitness(np.array(results).reshape(1, -1))  # weighted combination of [P, R, mAP@.5, mAP@.5-.95]
                stop = stopper(epoch=epoch, fitness=fi)  # early stop check
                if fi > best_fitness:
                    best_fitness = fi
                log_vals = list(mloss) + list(results) + lr

                # Save model
                if (not cfg.model.nosave) or final_epoch:  # if save
                    ckpt = {
                        'epoch': epoch,
                        'best_fitness': best_fitness,
                        'model': deepcopy(de_parallel(self.model)).half(),
                        'ema': deepcopy(ema.ema).half(),
                        'updates': ema.updates,
                        'optimizer': optimizer.state_dict(),
                        'opt': vars(cfg.model),
                        'git': GIT_INFO,  # {remote, branch, commit} if a git repo
                        'date': datetime.now().isoformat()}

                    # Save last, best and delete
                    torch.save(ckpt, self.last)
                    if best_fitness == fi:
                        torch.save(ckpt, self.best)
                    if cfg.model.save_period > 0 and epoch % cfg.model.save_period == 0:
                        torch.save(ckpt, self.w / f'epoch{epoch}.pt')
                    del ckpt
            
            # EarlyStopping
            if RANK != -1:  # if DDP training
                broadcast_list = [stop if RANK == 0 else None]
                dist.broadcast_object_list(broadcast_list, 0)  # broadcast 'stop' to all ranks
                if RANK != 0:
                    stop = broadcast_list[0]
            if stop:
                break  # must break all DDP ranks
            # end epoch
        # End training
        if RANK in {-1, 0}:
            LOGGER.info(f'\n{epoch - start_epoch + 1} epochs completed in {(time.time() - t0) / 3600:.3f} hours.')
            for f in self.last, self.best:
                if f.exists():
                    if f is self.last:
                        strip_optimizer(f, self.last_striped)  # strip optimizers
                    else:
                        strip_optimizer(f, self.best_striped)  # strip optimizers
                    if f is self.best:
                        LOGGER.info(f'\nValidating {f}...')
                        results, _, _ = validate.run(
                            self.data_dict,
                            batch_size=cfg.model.batch // self.world_size * 2,
                            imgsz=imgsz,
                            model=attempt_load(f, self.set_device).half(),
                            dataloader=val_loader,
                            save_dir=self.save_dir,
                            verbose=True,
                            plots=True,
                            compute_loss=compute_loss)  # val best model with plots
        torch.cuda.empty_cache()
        return results
    
    def do_detect(self, cfg: DictConfig):
        source = str(cfg.predict.source)
        is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
        if is_file == False:
            LOGGER.error('source file error!')
            return None
        # Load model
        model = DetectMultiBackend(cfg.predict.weights, device=self.set_device, dnn=cfg.predict.dnn, data=cfg.predict.data, fp16=cfg.predict.half)
        stride, names, pt = model.stride, model.names, model.pt
        imgsz = check_img_size(cfg.predict.imgsz, s=stride)  # check image size
        # Load data
        bs = 1  # batch_size
        dataset = LoadImages(source, img_size=imgsz, stride=stride, auto=pt, vid_stride=cfg.predict.vid_stride)
        vid_path, vid_writer = [None] * bs, [None] * bs

        # Run inference
        model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
        seen, windows, dt = 0, [], (Profile(), Profile(), Profile())
        for path, im, im0s, vid_cap, s in dataset:
            with dt[0]:
                im = torch.from_numpy(im).to(model.device)
                im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
                im /= 255  # 0 - 255 to 0.0 - 1.0
                if len(im.shape) == 3:
                    im = im[None]  # expand for batch dim

            # Inference
            with dt[1]:
                pred = model(im, augment=cfg.predict.augment, visualize=cfg.predict.visualize)

            # NMS
            set_classes = None if cfg.predict.classes == 'all' else cfg.predict.classes
            with dt[2]:
                pred = non_max_suppression(pred, cfg.predict.conf_thres, cfg.predict.iou_thres, set_classes, cfg.predict.agnostic_nms, max_det=cfg.predict.max_det)

            # Second-stage classifier (optional)
            # pred = utils.general.apply_classifier(pred, classifier_model, im, im0s)

            # Process predictions
            for i, det in enumerate(pred):  # per image
                seen += 1
                p, im0, frame = path, im0s.copy(), getattr(dataset, 'frame', 0)

                p = Path(p)  # to Path
                save_path = str(Path(cfg.predict.save_dir) / p.name)  # im.jpg
                txt_path = str(Path(cfg.predict.save_dir) / 'labels' / p.stem) + ('' if dataset.mode == 'image' else f'_{frame}')  # im.txt
                s += '%gx%g ' % im.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                imc = im0  # for save_crop
                annotator = Annotator(im0, line_width=cfg.predict.line_thickness, example=str(names))
                if len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_boxes(im.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, 5].unique():
                        n = (det[:, 5] == c).sum()  # detections per class
                        s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if cfg.predict.save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            line = (cls, *xywh, conf) # label format
                            with open(f'{txt_path}.txt', 'a') as f:
                                f.write(('%g ' * len(line)).rstrip() % line + '\n')
                        if cfg.predict.save_img or cfg.predict.save_crop or cfg.predict.view_img:  # Add bbox to image
                            c = int(cls)  # integer class
                            label = f'{names[c]} {conf:.2f}'
                            annotator.box_label(xyxy, label)

                # Stream results
                im0 = annotator.result()
                if cfg.predict.view_img:
                    if platform.system() == 'Linux' and p not in windows:
                        windows.append(p)
                        cv2.namedWindow(str(p), cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)  # allow window resize (Linux)
                        cv2.resizeWindow(str(p), im0.shape[1], im0.shape[0])
                    cv2.imshow(str(p), im0)
                    cv2.waitKey(1)  # 1 millisecond

                # Save results (image with detections)
                if cfg.predict.save_img:
                    if dataset.mode == 'image':
                        cv2.imwrite(save_path, im0)
                    else:  # 'video' or 'stream'
                        if vid_path[i] != save_path:  # new video
                            vid_path[i] = save_path
                            if isinstance(vid_writer[i], cv2.VideoWriter):
                                vid_writer[i].release()  # release previous video writer
                            if vid_cap:  # video
                                fps = vid_cap.get(cv2.CAP_PROP_FPS)
                                w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                                h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                            else:  # stream
                                fps, w, h = 30, im0.shape[1], im0.shape[0]
                            save_path = str(Path(save_path).with_suffix('.mp4'))  # force *.mp4 suffix on results videos
                            vid_writer[i] = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
                        vid_writer[i].write(im0)