_base_ = [
    '/home/tureckova/Code/mmsegmentation/configs/_base_/models/fcn_unet_s5-d16.py',
    'tomato360-segmentation.py',
    '/home/tureckova/Code/mmsegmentation/configs/_base_/default_runtime.py',
    '/home/tureckova/Code/mmsegmentation/configs/_base_/schedules/schedule_160k.py'
]
img_mean = [105.80011097, 115.17593129, 92.22527362]
img_std = [69.41639875, 66.94051085, 75.33822364]

model = dict(
    decode_head=dict(num_classes=1,
                     out_channels=1,
                     align_corners=True
                     # loss_decode=dict(
                     #     type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0)
                     ),
    auxiliary_head=dict(num_classes=1,
                        out_channels=1,
                        align_corners=True
                        # loss_decode=dict(
                        #     type='CrossEntropyLoss', use_sigmoid=True, loss_weight=0.4)
                        ),
    # # data preprocessor
    data_preprocessor=dict(size=[512,512]),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='slide', crop_size=(512,512), stride=(400, 400)))

val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
test_evaluator = val_evaluator

work_dir = '/mnt/SSD1TB/TACR_TREND/models/tomato_row/fcn_unet-512x512-tomato360v2.1-3.0/'