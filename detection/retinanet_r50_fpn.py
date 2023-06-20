_base_ = [
    '/home/tureckova/PycharmProjects/mmdetection/configs/' + '/_base_/models/retinanet_r50_fpn.py',
    'tomato360-oneclass.py',
    '/home/tureckova/PycharmProjects/mmdetection/configs/' + '/_base_/schedules/schedule_2x.py',
    '/home/tureckova/PycharmProjects/mmdetection/configs/' + '/_base_/default_runtime.py'
]
model = dict(
    bbox_head=dict(num_classes=3))
# optimizer
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001))
vis_backends = [
    dict(type='LocalVisBackend'),
    dict(type='TensorboardVisBackend')
]
visualizer = dict(
    type='DetLocalVisualizer',
    vis_backends=vis_backends,
    name='visualizer')
work_dir = '/home/tureckova/Pictures/tomato360/models/tomato_row/360ann_v2.1_retinanet_r50_fpn_1x/assahi-1class-2x/'