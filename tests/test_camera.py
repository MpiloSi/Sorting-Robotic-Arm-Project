import unittest
import cv2
from robodk import robolink  # Correct import
from src.camera import CameraHandler

class TestCameraHandler(unittest.TestCase):
    def setUp(self):
        """Set up the RoboDK connection and CameraHandler instance."""
        self.RDK = robolink.Robolink()  # Use robolink.Robolink()
        self.camera_item = self.RDK.Item('Camera')  # Replace with your camera's name
        self.camera_handler = CameraHandler(self.camera_item)

    def test_capture_image(self):
        """Test if the camera can capture an image."""
        image = self.camera_handler.capture_image()
        self.assertIsNotNone(image, "Captured image should not be None")
        self.assertGreater(image.shape[0], 0, "Captured image height should be greater than 0")
        self.assertGreater(image.shape[1], 0, "Captured image width should be greater than 0")

    def test_display_image(self):
        """Test if the image display function works without errors."""
        image = self.camera_handler.capture_image()
        try:
            self.camera_handler.display_image(image)
        except Exception as e:
            self.fail(f"Displaying image raised an exception: {e}")

    def tearDown(self):
        """Release the camera resources after tests."""
        self.camera_handler.release()

if __name__ == '__main__':
    unittest.main()