# dataset settings
dataset_type = 'CocoDataset'
data_root = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/cuts/'#'/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/cut_2042x2042_masks/'
classes = ('green', 'orange', 'red')
backend_args = None


train_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(1024, 1024), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(1024, 1024), keep_ratio=True),
    # If you don't have a gt annotation, delete the pipeline
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]
train_dataloader = dict(
    batch_size=4,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(classes=classes),
        data_root=data_root + 'train_images_512_02/', #'train_images_2042_02/',
        ann_file=data_root + 'train_512_02.json', #'train_2042_02.json',
        data_prefix=dict(img=''),
        pipeline=train_pipeline))
val_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(classes=classes),
        data_root=data_root + 'val_images_512_02/', #'val_images_2042_02/',
        ann_file=data_root + 'val_512_02.json', #'val_2042_02.json',
        data_prefix=dict(img=''),
        pipeline=test_pipeline))
test_dataloader = dict(
    batch_size=1,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(classes=classes),
        data_root=data_root + 'test_images_512_02/', #'test_images_2042_02/',
        ann_file=data_root + 'test_512_02.json', #'test_2042_02.json',
        data_prefix=dict(img=''),
        pipeline=test_pipeline))

val_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'val_512_02.json', #'val_2042_02.json',
    metric='bbox',
    format_only=False,
    backend_args=backend_args)
test_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'test_512_02.json', #'test_2042_02.json',
    metric='bbox',
    format_only=False,
    classwise=True,
    backend_args=backend_args)

# inference on test dataset and
# format the output results for submission.
# test_dataloader = dict(
#     batch_size=1,
#     num_workers=2,
#     persistent_workers=True,
#     drop_last=False,
#     sampler=dict(type='DefaultSampler', shuffle=False),
#     dataset=dict(
#         type=dataset_type,
#         data_root=data_root,
#         ann_file=data_root + 'annotations/image_info_test-dev2017.json',
#         data_prefix=dict(img='test2017/'),
#         test_mode=True,
#         pipeline=test_pipeline))
# test_evaluator = dict(
#     type='CocoMetric',
#     metric='bbox',
#     format_only=True,
#     ann_file=data_root + 'annotations/image_info_test-dev2017.json',
#     outfile_prefix='./work_dirs/coco_detection/test')