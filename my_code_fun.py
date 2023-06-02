import torch
from PIL import Image

def detect_defect(image_path):
    img = Image.open(image_path)

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt')

    results = model([img], size=640)

    return results.xyxy[0]

image_path = 'E:\yolov5-master\yolov5-master\data\images\defect_image_1.jpg'  
detection_results = detect_defect(image_path)
print(detection_results)

!pip install -r requirements.txt