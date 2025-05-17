import torch
import torchvision
from torchvision.models.detection import FasterRCNN
from torchvision.transforms import functional as F
from PIL import Image

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

image_path = "C:/Users/user/Desktop/data/06.jpg"
image = Image.open(image_path)

image_tensor = F.to_tensor(image).unsqueeze(0)

with torch.no_grad():
    prediction = model(image_tensor)

boxes = prediction[0]['boxes']
scores = prediction[0]['scores']
labels = prediction[0]['labels']

for box, score, label in zip(boxes, scores, labels):
    print(f"Label: {label}, Score: {score:.2f}, Box: {box}")