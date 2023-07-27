from flask import Flask, request
from ultralytics import YOLO
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
        save_image(file)  # 들어오는 이미지 저장
        test_img = './temp/' + file.filename
        result = model(test_img, conf=0.5, save=True, line_thickness=1)

        cv2.imshow("result", cv2.imread('C:/fishproject/runs/detect/predict/'+file.filename))
        cv2.waitKey(0)

        return "1"


if __name__ == '__main__':
    app.run()