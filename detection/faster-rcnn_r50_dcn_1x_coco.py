_base_ = [
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/models/faster-rcnn_r50_fpn.py',
    'tomato360-bbox.py',
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/schedules/schedule_1x.py',
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/default_runtime.py'
]
model = dict(
    backbone=dict(
        dcn=dict(type='DCN', deform_groups=1, fallback_on_stride=False),
        stage_with_dcn=(False, True, True, True)),
    roi_head=dict(bbox_head=dict(num_classes=3)))

work_dir = '/mnt/SSD1TB/TACR_TREND/models/tomato_row/360ann_v2.1_faster-rcnn_r50_dcn_1x/fold-1-3class/'