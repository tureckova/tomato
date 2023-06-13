# dataset settings
dataset_type = 'BaseSegDataset'
data_dir = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/segm/'
img_dir = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/cut_2042x2042/'
mask_dir = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/mask_2042x2042/'
split_dir = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/v2.1/5-fold/fold-0/'
img_norm_cfg = dict(
    mean=[105.80011097, 115.17593129, 92.22527362], std=[69.41639875, 66.94051085, 75.33822364], to_rgb=True)
img_scale = (512, 512)
CLASSES = ('background', 'tomato')
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(
        type='RandomResize',
        scale=img_scale,
        ratio_range=(1., 1.),
        keep_ratio=True),
    #dict(type='RandomCrop', crop_size=img_scale, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='PackSegInputs')
]

val_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=img_scale, keep_ratio=True),
    dict(type='LoadAnnotations', reduce_zero_label=False),
    dict(type='PackSegInputs')
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=img_scale, keep_ratio=True),
    dict(type='LoadAnnotations', reduce_zero_label=False),
    dict(type='PackSegInputs')
]

img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
tta_pipeline = [
    dict(type='LoadImageFromFile', backend_args=None),
    dict(
        type='TestTimeAug',
        transforms=[
            # [
            #     dict(type='Resize', scale_factor=r, keep_ratio=True)
            #     for r in img_ratios
            # ],
            [
                dict(type='RandomFlip', prob=0., direction='horizontal'),
                dict(type='RandomFlip', prob=1., direction='horizontal')
            ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
        ])
]

train_dataloader = dict(
    batch_size=4,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_root=data_dir,
        data_prefix=dict(
            img_path='img_dir/train/', seg_map_path='ann_dir/train/'),
        reduce_zero_label=True,
        pipeline=train_pipeline))

val_dataloader = dict(
    batch_size=4,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_root=data_dir,
        data_prefix=dict(
            img_path='img_dir/val/', seg_map_path='ann_dir/val/'),
        reduce_zero_label=True,
        pipeline=val_pipeline))

test_dataloader = dict(
    batch_size=4,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_root=data_dir,
        data_prefix=dict(
            img_path='img_dir/test-whole/', seg_map_path='ann_dir/test-whole/'),
        reduce_zero_label=True,
        pipeline=train_pipeline))
