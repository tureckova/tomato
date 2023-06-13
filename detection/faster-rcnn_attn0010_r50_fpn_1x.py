_base_ = [
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/models/faster-rcnn_r50_fpn.py',
    'tomato360-bbox.py',
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/schedules/schedule_1x.py',
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/default_runtime.py'
]


model = dict(
    backbone=dict(plugins=[
        dict(
            cfg=dict(
                type='GeneralizedAttention',
                spatial_range=-1,
                num_heads=8,
                attention_type='0010',
                kv_stride=2),
            stages=(False, False, True, True),
            position='after_conv2')
    ]),
    roi_head=dict(bbox_head=dict(num_classes=3)))

work_dir = '/mnt/SSD1TB/TACR_TREND/models/tomato_row/360ann_v2.1_faster-rcnn_attn0010_r50_fpn_1x/fold-1-3class/'
