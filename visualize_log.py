import json
import matplotlib.pyplot as plt
scalar_folder = '/mnt/SSD1TB/TACR_TREND/models/tomato_row/360ann_v2.2_tood_r50_dcn_fpn_1x/assahi-1class-24epoch-5-fold/fold-4/20230720_162136/vis_data/'
scalar_json = scalar_folder + 'scalars.json'

# 1. Load the JSON data into Python
with open(scalar_json, "r") as f:
    lines = f.readlines()
    data = [json.loads(line) for line in lines]

# Extract and organize training data
epoch_loss = {}
epoch_loss_cls = {}
epoch_loss_bbox = {}

for entry in data:
    if 'loss' in entry:
        epoch = entry['epoch']
        if epoch not in epoch_loss or entry['iter'] > epoch_loss[epoch][0]:
            epoch_loss[epoch] = (entry['iter'], entry['loss'])
            epoch_loss_cls[epoch] = (entry['iter'], entry['loss_cls'])
            epoch_loss_bbox[epoch] = (entry['iter'], entry['loss_bbox'])

# Extract validation data
bbox_mAP = []
bbox_mAP_50 = []

for entry in data:
    if 'coco/bbox_mAP' in entry:
        bbox_mAP.append(entry['coco/bbox_mAP'])
        bbox_mAP_50.append(entry['coco/bbox_mAP_50'])

# Plotting
epochs = sorted(epoch_loss.keys())
training_loss = [epoch_loss[e][1] for e in epochs]
loss_cls_values = [epoch_loss_cls[e][1] for e in epochs]
loss_bbox_values = [epoch_loss_bbox[e][1] for e in epochs]

plt.figure(figsize=(12, 6))

# First graph for training losses
plt.subplot(1, 2, 1)
plt.plot(epochs, training_loss, label='Training Loss', color='blue')
plt.plot(epochs, loss_cls_values, label='Loss Cls', color='green')
plt.plot(epochs, loss_bbox_values, label='Loss Bbox', color='red')
plt.title('Training Losses based on Epoch')
plt.xlabel('Epochs')
#plt.xlim([min(epochs), max(epochs)])
plt.ylabel('Loss Value')
plt.legend()
plt.grid(True)

# Second graph for validation metrics
plt.subplot(1, 2, 2)
plt.plot(epochs, bbox_mAP, label='bbox mAP', color='purple')
plt.plot(epochs, bbox_mAP_50, label='bbox mAP @0.50', color='orange')
plt.title('Validation Metrics based on Epoch')
plt.xlabel('Epochs')
plt.ylabel('Metric Value')
plt.ylim([0,1])
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig(scalar_folder + 'train-val-loss.png')

