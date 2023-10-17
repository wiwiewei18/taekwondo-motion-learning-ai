from ultralytics import YOLO
import shutil

shutil.rmtree('./runs', ignore_errors=True)

model = YOLO('yolov8n-cls.pt')  # Pretrained model (recommended for training)

model.train(data='./dataset', epochs=20, imgsz=64)