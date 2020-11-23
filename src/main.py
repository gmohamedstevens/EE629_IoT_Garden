from sensor import *
from database import *
from control import *

pumpControl = Pump()
lampControl = Lamp()
cameraControl = Camera()

# MAIN PROGRAM LOOP
mainLoopFlag = True
while(mainLoopFlag):

    cameraControl.takePhoto()
    mainLoopFlag = False


# TEST SECTION
if lampControl.lampIsOn():
    print("Lamp is on")
else:
    print("Lamp is off")

lampControl.turnOnLamp()
if lampControl.lampIsOn():
    print("Lamp is on")
else:
    print("Lamp is off")