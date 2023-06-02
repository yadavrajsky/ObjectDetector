import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import utils
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

#old code

#!unzip / content / drive / MyDrive / fabric - defects - detection - YOLOv5 / dataset / dataset.zip - d / content / yolov5 / dataset_dum_dum 

#new code
import zipfile

zip_path = 'C://Users//vikas//Downloads//dataset.zip'
target_dir = 'yolov5/dataset_dum_dum'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(target_dir)

# till here 

img1 = Image.open('E:/yolov5-master/datasets/dataset/train/images/010751.jpg')
img2 = Image.open('E:/yolov5-master/datasets/dataset/train/images/010782.jpg')
img3 = Image.open('E:/yolov5-master/datasets/dataset/train/images/086852.jpg')
img4 = Image.open('E:/yolov5-master/datasets/dataset/train/images/010774.jpg')
#plotting later 
"""

plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(img1)
plt.subplot(2, 2, 2)
plt.imshow(img2)
plt.subplot(2, 2, 3)
plt.imshow(img3)
plt.subplot(2, 2, 4)
plt.imshow(img4)

plt.show()
"""

os.rename('yolov5/dataset_dum_dum/dataset', 'yolov5/dataset')
_, _, files1 = next(os.walk("yolov5/dataset/train/images"))
print("Number of Samples in Train Data: ", len(files1))
_, _, files2 = next(os.walk("yolov5/dataset/valid/images"))
print("Number of Samples in Validation Data: ", len(files2))

print("Train : Valid ::", len(files1) / (len(files1) + len(files2)), ":", len(files2) / (len(files1) + len(files2)))
TRAIN = True
EPOCHS = 3000
'''
!python train.py - -img 640 - -batch 16 - -epochs {EPOCHS} - -data dataset / data.yaml - -weights yolov5m.pt

%pwd
!python detect.py - -weights runs / train / exp / weights / best.pt - -img 640 - -data .. / content / yolov5 / dataset / data.yaml - -source .. / yolov5 / dataset / valid / images / 010815.jpg
!python detect.py - -weights runs / train / exp / weights / best.pt - -img 640 - -data .. / content / yolov5 / dataset / data.yaml - -source .. / yolov5 / dataset / valid / images / 010805.jpg
!python detect.py - -weights runs / train / exp / weights / best.pt - -img 640 - -data .. / content / yolov5 / dataset / data.yaml - -source .. / yolov5 / dataset / valid / images / 010820.jpg

%matplotlib inline
img = cv2.imread("runs/detect/exp4/010815.jpg")
plt.imshow(img)
plt.show()

%matplotlib inline
img = cv2.imread("runs/detect/exp8/010805.jpg")
plt.imshow(img)
plt.show()

%matplotlib inline
img = cv2.imread("runs/detect/exp10/010820.jpg")
plt.imshow(img)
plt.show()

!cp - r / content / yolov5 / runs / content / drive / MyDrive / yolov5_runs

results = pd.read_csv('/content/yolov5/runs/train/exp/results.csv')

results.columns = results.columns.str.strip()

results.columns
'''