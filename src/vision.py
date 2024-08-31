import cv2
import numpy as np
from src.config import COLOR_RANGES, SHAPE_TEMPLATES

class VisionProcessor:
    def __init__(self):
        # Load color ranges and shape templates from the configuration
        self.color_ranges = COLOR_RANGES
        self.shape_templates = SHAPE_TEMPLATES
        
    def detect_objects(self, image):
        detected_objects = []
        
        # Detect objects based on color
        color_objects = self.detect_color_objects(image)
        detected_objects.extend(color_objects)
        
        # Detect objects based on shape
        shape_objects = self.detect_shape_objects(image)
        detected_objects.extend(shape_objects)
        
        return detected_objects
    
    def detect_color_objects(self, image):
        color_objects = []
        
        for color, color_range in self.color_ranges.items():
            # Create a mask for the color range
            mask = cv2.inRange(image, np.array(color_range['lower']), np.array(color_range['upper']))
            # Find contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                color_objects.append({
                    'type': 'color',
                    'color': color,
                    'bbox': (x, y, w, h)
                })
        
        return color_objects
    
    def detect_shape_objects(self, image):
        shape_objects = []
        
        for shape, template in self.shape_templates.items():
            # Perform template matching
            res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            
            # Filter based on matching threshold
            if max_val > 0.5:  # Threshold can be adjusted
                x, y = max_loc
                h, w = template.shape[:2]
                shape_objects.append({
                    'type': 'shape',
                    'shape': shape,
                    'bbox': (x, y, w, h)
                })
        
        return shape_objects
    
    def draw_bounding_boxes(self, image, detected_objects):
        for obj in detected_objects:
            x, y, w, h = obj['bbox']
            color = (0, 255, 0) if obj['type'] == 'color' else (255, 0, 0)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, obj['type'], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return image
