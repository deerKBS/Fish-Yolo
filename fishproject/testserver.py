from flask import Flask, request
from ultralytics import YOLO
from PIL import Image
import cv2

app = Flask(__name__)
model = YOLO('C:/Users/SSAFY/Desktop/fish/runs/detect/train12/weights/best.pt')

# POST 통신으로 들어오는 이미지를 저장하고 모델로 추론하는 과정
def save_image(file):
    file.save('./temp/'+ file.filename)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file)
        result = model(img, conf=0.5, line_thickness=1, save=False)

        # cv2.imshow("result", r_img[0])
        # cv2.waitKey(0)

        return "1"


if __name__ == '__main__':
    app.run()