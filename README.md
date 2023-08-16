# Fish-Yolo

- Yolov8
- tensorflow
- Fast API
- Google ARCore for length measurement

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
- 도감 등록 후 알림 (SSE)


### DataSet
https://universe.roboflow.com/baesung-koo-wzsdb/fish-detection-mv7xg

---

- IOS Lidar sensor를 사용한 Object 거리 측정 (SSAFY라서 IOS 포기)
  - https://developer.apple.com/forums/thread/709872
  - https://developer.apple.com/documentation/avfoundation/additional_data_capture/capturing_depth_using_the_lidar_camera?language=objc
  - https://mrousavy.com/blog/Camera-APIs-on-Android
  - https://github.com/mrousavy/react-native-vision-camera
 
- Google ARCore (Android Studio)

  ---
  - 1500장 수집 및 라벨링 (전처리로 4500장 이상)
  - Yolov8n 모델 학습
  - Flask에서 FastAPI 서버로 변경
    - pip install fastapi
    - pip install "uvicorn[standard]"
    - pip install ultralytics
    - pip install python-multipart
    - pip install torch
    - pip install tensorflow
  - ARCore 자동 초점 미지원 관계로 초점이 맞지 않는 이미지로 추가학습 필요 및 예정
---


