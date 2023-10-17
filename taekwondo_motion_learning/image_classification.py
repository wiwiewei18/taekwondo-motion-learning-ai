from flask import Blueprint, request
from werkzeug.utils import secure_filename
import os
import uuid

from taekwondo_motion_learning.machine_learning.image_classification import predict

bp = Blueprint('image_classification', __name__)

@bp.route('/classify-taekwondo-movement-image', methods=('POST',))
def classify_taekwondo_movement_image():
    image = request.files['image']
    uniqueId = uuid.uuid4()
    savedImageDir = f"./taekwondo_motion_learning/temp/{secure_filename(str(uniqueId) + image.filename)}"
    
    image.save(savedImageDir)

    prediction = predict.classifyImage(savedImageDir)

    os.remove(savedImageDir)
    
    return prediction