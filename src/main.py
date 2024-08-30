import cv2
from robodk import *
from src.camera import CameraHandler
from src.vision import VisionProcessor
from src.robot_control import RobotController
from src.sorting_logic import SortingLogic

def main():
    # Initialize RoboDK environment
    RDK = Robolink()
    
    # Get the robotic arm and camera objects
    robot = RDK.Item('Robot')
    camera = RDK.Item('Camera')
    
    # Create instances of the necessary modules
    camera_handler = CameraHandler(camera)
    vision_processor = VisionProcessor()
    robot_controller = RobotController(robot)
    sorting_logic = SortingLogic()
    
    while True:
        # Capture an image from the camera
        image = camera_handler.capture_image()
        
        # Process the image to detect objects
        detected_objects = vision_processor.detect_objects(image)
        
        # Apply sorting logic to the detected objects
        sorted_objects = sorting_logic.sort_objects(detected_objects)
        
        # Control the robotic arm to sort the objects
        robot_controller.sort_objects(sorted_objects)
        
        # Display the processed image (optional)
        processed_image = vision_processor.draw_bounding_boxes(image, detected_objects)
        cv2.imshow('Sorted Objects', processed_image)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources and close windows
    camera_handler.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()