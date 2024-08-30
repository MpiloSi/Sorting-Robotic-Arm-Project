import cv2
import numpy as np
from src.config import COLOR_RANGES, SHAPE_TEMPLATES

class VisionProcessor:
    def __init__(self):
        self.color_ranges = COLOR_RANGES
        self.shape_templates = SHAPE_TEMPLATES
        
    def detect_objects(self, image):
        detected_objects = []
        
        # Detect objects by color
        color_objects = self.detect_color_objects(image)
        detected_objects.extend(color_objects)
        
        # Detect objects by shape
        shape_objects = self.detect_shape_objects(image)
        detected_objects.extend(shape_objects)
        
        return detected_objects
    
    def detect_color_objects(self, image):
        color_objects = []
        
        for color, color_range in self.color_ranges.items():
            mask = cv2.inRange(image, np.array(color_range['lower']), np.array(color_range['upper']))
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
            res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            _, _, _, max_loc = cv2.minMaxLoc(res)
            
            x, y = max_loc
            w, h = template.shape[::-1]
            shape_objects.append({
                'type': 'shape',
                'shape': shape,
                'bbox': (x, y, w, h)
            })
        
        return shape_objects