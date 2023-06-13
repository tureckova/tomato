_base_ = [
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/models/faster-rcnn_r50_fpn.py',
    'tomato360-bbox-assahi-oneclass.py',
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/schedules/schedule_1x.py',
    '/home/tureckova/Code/mmdetection/configs' + '/_base_/default_runtime.py'
]
model = dict(
    roi_head=dict(bbox_head=dict(num_classes=3)))
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001))
vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='TensorboardVisBackend')
]
visualizer = dict(
    type='DetLocalVisualizer',
    vis_backends=vis_backends,
    name='visualizer')
work_dir = '/mnt/SSD1TB/TACR_TREND/models/tomato_row/360ann_v2.1_faster-rcnn_r50_fpn_1x/assahi-512cuts-oneclass/'