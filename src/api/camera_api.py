import cv2

class CameraAPI:
    def __init__(self, camera_index=0):
        """
        Initialize the camera with the specified camera index.
        Defaults to the first camera (index 0).
        """
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)

        # Check if the camera opened successfully
        if not self.cap.isOpened():
            raise ValueError(f"Cannot open camera with index {self.camera_index}")

    def capture_image(self):
        """
        Capture an image from the camera and return it.
        """
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture image from the camera")

        return frame

    def release_camera(self):
        """
        Release the camera resource.
        """
        if self.cap.isOpened():
            self.cap.release()

    def save_image(self, file_path):
        """
        Capture an image and save it to the specified file path.
        """
        frame = self.capture_image()
        cv2.imwrite(file_path, frame)

    def __del__(self):
        """
        Ensure the camera is released when the object is destroyed.
        """
        self.release_camera()

# Example usage:
# camera = CameraAPI(camera_index=0)
# image = camera.capture_image()
# camera.save_image("captured_image.jpg")
