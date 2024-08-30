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
        conf = 0.3,
        show_labels = False,
        classes = [9, 10],
        agnostic_nms = True
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
    img = cv2.putText(img, f'total: {counter}', (50, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    img = cv2.resize(img, (640, 640))
    cv2.imshow('result', img)
    cv2.waitKeyEx(0)

def result_without_label(file_path):
    res = model.predict(
        source=file_path,
        imgsz = 640,
        conf = 0.3,
        show_labels = False,
        classes = [9, 10],
        agnostic_nms = True
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

    img = res[0].plot(labels=False, probs=False)
    img = cv2.resize(img, (640, 640))
    img = cv2.putText(img, f'total: {counter}', (50, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('result', img)
    cv2.waitKeyEx(0)
