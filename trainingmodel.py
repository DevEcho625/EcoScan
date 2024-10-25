from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")

results = model.train(data = "Dataset", epochs=100, imgsz =640)
