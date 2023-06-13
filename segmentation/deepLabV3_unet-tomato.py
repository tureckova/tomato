_base_ = [
    '/home/tureckova/Code/mmsegmentation/configs/_base_/models/deeplabv3_unet_s5-d16.py',
    'tomato360-segmentation.py',
    '/home/tureckova/Code/mmsegmentation/configs/_base_/default_runtime.py',
    '/home/tureckova/Code/mmsegmentation/configs/_base_/schedules/schedule_160k.py'
]

model = dict(
    decode_head=dict(num_classes=2,
                     out_channels=1,
                     loss_decode=dict(
                         type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0)
                     ),
    auxiliary_head=dict(num_classes=2,
                        out_channels=1,
                        loss_decode=dict(
                            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=0.4)
                        ),
    # model training and testing settings
    train_cfg=dict(),
    test_cfg=dict(mode='whole'))

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
)
work_dir = '/home/tureckova/Pictures/tomato360/models/tomato_row/deepLabV3_unet-512x512-tomato360v2.1/'