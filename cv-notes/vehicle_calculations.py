import cv2
import numpy as np
import math
import torch

cap = cv2.VideoCapture("Cars.mp4")

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

count = 0
center_points_prev_frame = []

tracking_objects = []
track_id = 0

cnt = 0

while True:
    ret, frame = cap.read()
    results = model(frame)
    width = frame.shape[1]
    height = frame.shape[0]
    #targetY = int(0.6 * height)
    for result in results.xyxy[0]:
        #print()
        if (int(result[3]) == int(0.6 * height) or int(result[3]) == int(0.6 * height) - 1) and (result[5] == 2 or result[5] == 5):
            cv2.rectangle(frame, (int(result[0]), int(result[1])), (int(result[2]), int(result[3])), (0, 255, 0), 2)
            cnt += 1

        if int(result[3]) >= int(0.6 * height - 2):
            cv2.rectangle(frame, (int(result[0]), int(result[1])), (int(result[2]), int(result[3])), (0, 255, 0), 2)


    cv2.line(frame, (0, int(0.6 * height)), (width, int(0.6 * height)), (0, 255, 0), 2)
    cv2.putText(frame, "count:"+str(cnt), (30, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.imshow("video", frame)


    if cv2.waitKey(1) == ord("q"):
        break