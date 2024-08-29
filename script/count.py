from ultralytics import YOLO
import time
import cv2
import torch

model = YOLO('../betst2.pt')

def result(file_path):
    res = model(file_path)
    # print(res[0].boxes.data)
    counter = len(res[0].boxes.data)
    image = cv2.imread(file_path)
    window_name = 'Image'

    img = cv2.imread(file_path)
    img = cv2.putText(img, f'total vehicels: {counter}', (50, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)
    img = cv2.resize(img, (640, 640))
    cv2.imshow('result', img)
    cv2.waitKeyEx(0)

