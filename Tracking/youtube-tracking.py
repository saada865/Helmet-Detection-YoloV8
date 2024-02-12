from ultralytics import YOLO

model = YOLO('/Users/saadahmadmalik/Downloads/yolov8n.pt')
results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)