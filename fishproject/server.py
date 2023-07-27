import io
import json

from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request
import torch
from ultralytics import YOLO


app = Flask(__name__)
model = YOLO('C:/Users/SSAFY/Desktop/fish/runs/detect/train12/weights/best.pt')

# POST 통신으로 들어오는 이미지를 저장하고 모델로 추론하는 과정
def save_image(file):
    file.save('./temp/'+ file.filename)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        save_image(file)  # 들어오는 이미지 저장
        train_img = './temp/' + file.filename
        result = model(train_img)
        # print(result[0].boxes[0].cls[0].numpy())
        # print(result[0].boxes[0].xywh)
        print(len(result[0].boxes)) # detected objects count
        for box in result[0].boxes:
            print(box)
        return "success"


if __name__ == '__main__':
    app.run()