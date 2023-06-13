dataset_type = 'CocoDataset'
data_root = '/mnt/SSD1TBdrive/TACR_TREND/data/tomato_row/tomato360/cut_2042x2042_masks/'
split_root = '/mnt/SSD1TBdrive/TACR_TREND/data/tomato_row/tomato360/v2.1/5-fold/fold-0/'
classes = ('green', 'orange', 'red')
img_norm_cfg = dict(
    mean=[105.80011097, 115.17593129, 92.22527362], std=[69.41639875, 66.94051085, 75.33822364], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='Resize', img_scale=(1024, 1024), keep_ratio=True), #(height, width)
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1024, 1024),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='DefaultFormatBundle'),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=split_root + 'cut_2042x2042_train_coco.json',
        img_prefix=data_root,
        classes=classes,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=split_root + 'cut_2042x2042_val_coco.json',
        img_prefix=data_root,
        classes=classes,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=split_root + 'cut_2042x2042_test_coco.json',
        img_prefix=data_root,
        classes=classes,
        pipeline=test_pipeline))
evaluation = dict(metric=['bbox', 'segm'])
