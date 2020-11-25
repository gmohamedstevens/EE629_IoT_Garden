class Camera:
        # Object initialization
        def __init__(self):
                self.liveFeedPhoto = 1;
                self.cameraConnectedFlag = False;
                pass
        # Returns if a camera is connected to the Pi
        def isConnected(self):
                return self.cameraConnectedFlag
        # Take photo using webcam and return
        def takePhoto(self):
                print("SNAP! A photo has been taken")
                return 1
        # Update the live feed with a photo
        def updateLiveFeed(self, photo):
                self.liveFeedPhoto = photo
                print("Live feed updated")
        # Adds photo to the time lapse
        def addToTimeLapse(self, photo):
                print("Added photo to time-lapse")


class Sensor:
        # Object initialization
        def __init__(self, pin):
                self.GPIOPin = pin
        # Returns the reading of the sensor
        def read(self):
                pass
        # Return the GPIO pin the control is attached to
        def returnGPIOPin(self):
                return self.GPIOPin
        # Set the GPIO pin the control is attached to
        def setGPIOPin(self, pin):
                self.GPIOPin = pin