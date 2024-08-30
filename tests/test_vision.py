import unittest
import numpy as np
import cv2
from src.vision import VisionProcessor

class TestVisionProcessor(unittest.TestCase):
    def setUp(self):
        """Set up the VisionProcessor instance."""
        self.vision_processor = VisionProcessor()
        
        # Create a simple test image (a red square on a white background)
        self.test_image = np.ones((400, 400, 3), dtype=np.uint8) * 255  # White background
        cv2.rectangle(self.test_image, (100, 100), (300, 300), (0, 0, 255), -1)  # Red square

    def test_detect_color_objects(self):
        """Test the color object detection functionality."""
        detected_objects = self.vision_processor.detect_color_objects(self.test_image)
        
        # Check if the detected objects contain the expected color
        self.assertGreater(len(detected_objects), 0, "Should detect at least one color object")
        self.assertEqual(detected_objects[0]['color'], 'red', "Detected color should be red")
        self.assertEqual(detected_objects[0]['type'], 'color', "Detected object type should be 'color'")
        
    def test_detect_shape_objects(self):
        """Test the shape object detection functionality."""
        # Assuming you have a shape template for matching
        # For this example, we will create a simple circle template
        circle_template = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.circle(circle_template, (50, 50), 40, (255, 255, 255), -1)  # White circle
        
        # Add the template to the vision processor for testing
        self.vision_processor.shape_templates = {'circle': circle_template}
        
        # Create a test image with a circle
        test_image_with_circle = np.ones((400, 400, 3), dtype=np.uint8) * 255  # White background
        cv2.circle(test_image_with_circle, (200, 200), 40, (255, 255, 255), -1)  # White circle
        
        detected_objects = self.vision_processor.detect_shape_objects(test_image_with_circle)
        
        # Check if the detected objects contain the expected shape
        self.assertGreater(len(detected_objects), 0, "Should detect at least one shape object")
        self.assertEqual(detected_objects[0]['shape'], 'circle', "Detected shape should be 'circle'")
        self.assertEqual(detected_objects[0]['type'], 'shape', "Detected object type should be 'shape'")

if __name__ == '__main__':
    unittest.main()