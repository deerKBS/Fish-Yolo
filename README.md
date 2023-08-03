# Fish-Yolo

- Yolov8
- tensorflow
- Fast API

### Fish Classes
- Red Sea Bream => 참돔
- Sea Bass => 농어
- Trout => 송어

---
### to do
- 데이터셋 수집 (추가)
- 라벨링 (추가)
- Train & test
  - 다양한 버전의 모델 학습 및 예측 시간 측정
  - 다양한 학습 방법 시도


### DataSet
https://universe.roboflow.com/baesung-koo-wzsdb/fish-detection-mv7xg

---

- IOS Lidar sensor를 사용한 Object 거리 측정 (SSAFY라서 IOS 포기)
  - https://developer.apple.com/forums/thread/709872
  - https://developer.apple.com/documentation/avfoundation/additional_data_capture/capturing_depth_using_the_lidar_camera?language=objc
  - https://mrousavy.com/blog/Camera-APIs-on-Android
  - https://github.com/mrousavy/react-native-vision-camera
 
- Google ARCore (Android Studio) try

  ---
  - 1500장 수집 및 라벨링 (전처리로 4500장 이상)
  - Yolov8n 모델 학습
  - 성능 평가 데이터 차후 업데이트
  - Flask에서 FastAPI 서버로 변경
