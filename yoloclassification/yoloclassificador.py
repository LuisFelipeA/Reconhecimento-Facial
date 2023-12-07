from ultralytics  import YOLO

# Train the model
model = YOLO('yolov8n-cls.pt')
#model = YOLO('/content/ultralytics/runs/classify/train/weights/best.pt')
model.train(data='../estagio/yoloclassification/dataset', epochs=10, imgsz=128)