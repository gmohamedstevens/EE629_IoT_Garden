import pygame.camera
from datetime import datetime

class Camera:
    
    width = 640
    height = 480
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0",(width,height))
    
    # Object initialization
    def __init__(self):
        self.liveFeedPhoto = 1;
        self.cameraConnectedFlag = False;
    # Starts the camera for capturing images
    def startCam(self):
        Camera.cam.start()
    # Stops the camera after image has been taken
    def stopCam(self):
        Camera.cam.stop()
    # Returns if a camera is connected to the Pi
    def isConnected(self):
        return self.cameraConnectedFlag
    # Take photo using webcam and return
    def takePhoto(self):
        image = Camera.cam.get_image()
        return image
    def timeStampPhoto(self, image):
        return image
    # Save a photo to memory
    def savePhoto(self, image, dest):
        pygame.image.save(image, dest)
    # Update the live feed with a photo
    def updateLiveFeed(self, photo):
        self.liveFeedPhoto = photo
        print("Live feed updated")
    # Adds photo to the time lapse
    def addToTimeLapse(self, photo):
        print("Added photo to time-lapse")
