from sensor import *
from database import *
from control import *

pumpControl = Pump(18)
lampControl = Lamp(24)
cameraControl = Camera()

tempSensor = Sensor(1)
lightSensor = Sensor(2)

# MAIN PROGRAM LOOP
mainLoopFlag = True
while(mainLoopFlag):
    # CAMERA CONTROL
    photo = cameraControl.takePhoto()
    cameraControl.addToTimeLapse(photo)
    cameraControl.updateLiveFeed(photo)
    # SENSOR CONTROL


    # DATABASE CONTROL


    mainLoopFlag = False


# TEST SECTION
print()
if lampControl.isOn():
    print("Lamp is on")
else:
    print("Lamp is off")

lampControl.turnOn()
if not lampControl.isOff():
    print("Lamp is on")
else:
    print("Lamp is off")

print()
print("The lamp is attached to GPIO pin " + str(lampControl.returnGPIOPin()))
print("The pump is attached to GPIO pin " + str(pumpControl.returnGPIOPin()))

print("The pump flow rate is " + str(pumpControl.returnFlowRate()))