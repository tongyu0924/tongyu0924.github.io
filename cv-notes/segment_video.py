import numpy as np
from skimage.io import imread, imsave
from sklearn.cluster import KMeans
import os
import cv2
import matplotlib.pyplot as plt

path = "C:/Users/user/Desktop/data/"
trainImage = []

for file in os.listdir(path)[:1000]:
    img = os.path.join(path, file)
    img = cv2.imread(img)
    img = cv2.resize(img, (256, 256))
    trainImage.append(img)

print
num_items = 1000
color_array = np.random.choice(range(256), 256 * 256 * 3).reshape(-1,3)
num_classes = 2
label_model = KMeans(n_clusters = num_classes)
label_model.fit(color_array)

img = cv2.imread('cars.png')
img = cv2.resize(img, (256, 256))
label_class = label_model.predict(img.reshape(-1,3)).reshape(256,256)

videoPath = 'Cars.mp4'
cap = cv2.VideoCapture(videoPath)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (256, 256))
    label_class = label_model.predict(frame.reshape(-1,3)).reshape(256,256)
    label_class = label_class.astype(np.float32)
    label_class = cv2.cvtColor(label_class, cv2.COLOR_RGBA2BGR)
    cv2.imshow("img", label_class)

    if cv2.waitKey(30) == ord("q"):
        break