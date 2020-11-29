# IoT Garden Monitor
# by Gamal Mohamed
# LIBRARIES USED:
# GPIOZero - Control of GPIO pins for sensors, lamp, pump, etc.
# CircuitPythonDHT - Reading temperature/humidity data from Adafruit DHT11 Sensor
# libgpiod2 - ???
# Board - Pin ids for DHT sensor

from sensor import *
from database import *
from control import *
from camera import *
from time import sleep

import board

##################
# INITIALIZATION #
##################
pumpControl = Pump("GPIO18")
lampControl = Lamp("GPIO24")
cameraControl = Camera()

tempSensor = DHTSensor(board.D16)
lightSensor = ACSensor("GPIO6", 1)

#####################
# MAIN PROGRAM LOOP #
#####################
mainLoopFlag = True
while(mainLoopFlag):
    ##########
    # CAMERA #
    ##########
    #photo = cameraControl.takePhoto()
    #cameraControl.addToTimeLapse(photo)
    #cameraControl.updateLiveFeed(photo)
    ##########
    # SENSOR #
    ##########
    print("Temperature")
    print(tempSensor.readTemperature())
    
    ############
    # DATABASE #
    ############

    #mainLoopFlag = False
    
################
# TEST SECTION #
################

print("Temperature")
#print(tempSensor.dhtDevice.temperature)
test = tempSensor.dhtDevice.temperature
