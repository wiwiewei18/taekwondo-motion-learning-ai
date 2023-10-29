from ultralytics import YOLO, settings
import shutil

shutil.rmtree('./runs', ignore_errors=True)

settings.update({'runs_dir': './runs'})

model = YOLO('yolov8n-cls.pt')  # Pretrained model (recommended for training)

model.train(data='./dataset', epochs=50, imgsz=64)