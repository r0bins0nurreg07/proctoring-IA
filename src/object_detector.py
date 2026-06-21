from ultralytics import YOLO

class ObjectDetector:
    def __init__(self):
        self.model = YOLO('yolov8n.pt')
        self.clases_prohibidas = ['cell phone', 'laptop', 'tablet']

    def detect_devices(self, frame):
        results = self.model(frame, verbose=False)
        device = []
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]
                if label in self.clases_prohibidas and float(box.conf[0]) > 0.5:
                    device.append(label)
        return device