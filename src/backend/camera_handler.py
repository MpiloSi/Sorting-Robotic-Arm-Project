import cv2

class CameraHandler:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)  # Initialize camera

    def capture_image(self):
        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Failed to capture image from camera")
        return frame  # Return captured frame

    def release_camera(self):
        self.camera.release()
