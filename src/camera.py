import cv2
from robodk import *

class CameraHandler:
    def __init__(self, camera_item):
        self.camera_item = camera_item
        self.cap = cv2.VideoCapture()
        self.cap.open(self.camera_item.CameraIndex())
        
    def capture_image(self):
        ret, frame = self.cap.read()
        if not ret:
            raise ValueError("Failed to capture image from camera")
        return frame
    
    def display_image(self, image, window_name='Camera Feed'):
        cv2.imshow(window_name, image)
        
    def release(self):
        self.cap.release()
