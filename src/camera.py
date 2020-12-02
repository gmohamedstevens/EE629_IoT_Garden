import pygame.camera
from datetime import datetime

class Camera(object):
    
    width = 640
    height = 480
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0",(width,height))
    
    # Object initialization
    def __init__(self):
        self.live_feed_photo = 1;
        self.camera_connected_flag = False;
    # Starts the camera for capturing images
    def start_cam(self):
        cls.cam.start()
    # Stops the camera after image has been taken
    def stop_cam(self):
        cls.cam.stop()
    # Returns if a camera is connected to the Pi
    def is_connected(self):
        return self.camera_connected_flag
    # Take photo using webcam and return
    def take_photo(self):
        image = cls.cam.get_image()
        return image
    # Add timestamp to photo of current time
    def time_stamp_photo(self, image):
        return image
    # Save a photo to memory
    def save_photo(self, image, dest):
        pygame.image.save(image, dest)
    # Update the live feed with a photo
    def update_live_feed(self, photo):
        self.live_feed_photo = photo
        print("Live feed updated")
    # Adds photo to the time lapse
    def add_to_time_lapse(self, photo):
        print("Added photo to time-lapse")
