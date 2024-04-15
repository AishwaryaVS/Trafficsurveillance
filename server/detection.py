from ultralytics import YOLO
# import cv2
from camera import Camera
import av

yolo_8 = YOLO()

def detect_from_video(camera: Camera):
    
    try:
        container = av.open(camera["VideoUrl"], timeout=1)
        frame = next(container.decode(video=0)).to_image()
    except Exception as e:
        camera["count"] = -1
        return camera
    
    detections = yolo_8(frame, verbose=False)
    count = 0
    
    for d in detections:
        class_list = [d.names[int(i)] for i in d.boxes.cls.tolist()]
        
        for c in class_list:
            if c in ["car", "truck", "bus", "motorcycle"]:
                count += 1
                
    camera["count"] = count
    return camera