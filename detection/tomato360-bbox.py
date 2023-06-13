# dataset settings
dataset_type = 'CocoDataset'
data_root = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/cut_2042x2042/'
split_root = '/mnt/SSD1TB/TACR_TREND/data/tomato_row/tomato360/v2.1/5-fold/fold-1/'
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
    batch_size=2,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(classes=classes),
        data_root=data_root,
        ann_file=split_root + 'cut_2042x2042_train_coco.json',
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
        data_root=data_root,
        ann_file=split_root + 'cut_2042x2042_val_coco.json',
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
        data_root=data_root,
        ann_file=split_root + 'cut_2042x2042_test_coco.json',
        data_prefix=dict(img=''),
        pipeline=test_pipeline))

val_evaluator = dict(
    type='CocoMetric',
    ann_file=split_root + 'cut_2042x2042_val_coco.json',
    metric='bbox',
    format_only=False,
    backend_args=backend_args)
test_evaluator = dict(
    type='CocoMetric',
    ann_file=split_root + 'cut_2042x2042_test_coco.json',
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