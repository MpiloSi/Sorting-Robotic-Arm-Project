import cv2
from robodk import *

class CameraHandler:
    def __init__(self, camera_item):
        self.camera_item = camera_item
        self.cap = self._initialize_camera()

    def _initialize_camera(self):
        # Example initialization code; adjust as needed based on RoboDK API
        camera_index = self.camera_item.getAttribute('CameraIndex')  # or use another method to get the camera index
        cap = cv2.VideoCapture(camera_index)
        return cap

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            return frame
        else:
            raise Exception("Failed to capture image")

    def display_image(self, image):
        cv2.imshow('Captured Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def release(self):
        self.cap.release()