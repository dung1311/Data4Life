from ultralytics import YOLO
import time
import cv2
import torch

model = YOLO('yolov8n-obb.pt')
model = YOLO('../best3.pt')

def result(file_path):
    res = model.predict(
        source=file_path,
        imgsz = 640,
        conf = 0.3
    )

    nums_vehicels = res[0]
    counter = 0
    if nums_vehicels.obb is not None and len(nums_vehicels.obb.cls > 0) :
        labels = nums_vehicels.obb.cls
        num_large_vehicles = (labels == 9).sum()
        num_small_vehicles = (labels == 10).sum()
        print(f'large vehicle: {num_large_vehicles}')
        print(f'small vehicle: {num_small_vehicles}')
        counter = num_large_vehicles + num_small_vehicles
        # print(counter)

    image = cv2.imread(file_path)
    window_name = 'Image'
    w, h, _ = image.shape
    img = cv2.imread(file_path)
    img = cv2.putText(img, f'total vehicels: {counter}', (50, 80), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2, cv2.LINE_AA)
    img = cv2.resize(img, (640, int(h*640/float(w))))
    cv2.imshow('result', img)
    cv2.waitKeyEx(0)

