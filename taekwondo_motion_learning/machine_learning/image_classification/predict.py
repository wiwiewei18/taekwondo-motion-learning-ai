from ultralytics import YOLO
import numpy as np

model = YOLO('./taekwondo_motion_learning/machine_learning/image_classification/runs/classify/train/weights/best.pt')

def classifyImage(image):
    results = model(image)
    classificationNames = results[0].names
    probs = results[0].probs.data.tolist()

    return {
        "result": classificationNames[np.argmax(probs)],
        "percentage": probs[np.argmax(probs)]*100
    }