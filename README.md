# Fish-Yolo

- Yolov8
- tensorflow
- Fast API

### Fish Classes
- 쏘가리 leopard mandarin fish
- 쥐노래미 Fat greenling
- 감성돔 black porgy
- 옥돔 Red tilefish
- 참돔 Red Seabream
- 송어 trout
- 돌돔 Doldom
- 말쥐치 Black scraper
---
### to do
1. flask -> fast api   (o)
2. gpu 사용 (o)
3. 안스 카메라 앱
4. 안스 <-> ai 서버 연결
5. 결과 화면에 표현
6. 도감 등록 구현


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
    - pip install fastapi
    - pip install "uvicorn[standard]"
    - pip install ultralytics
    - pip install python-multipart
    - pip install torch
    - pip install tensorflow

