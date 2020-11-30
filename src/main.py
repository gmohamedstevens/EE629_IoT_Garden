# IoT Garden Monitor
# by Gamal Mohamed
#
# LIBRARIES USED:
# GPIOZero - Control of GPIO pins for sensors, lamp, pump, etc. and reading MCP3008 channels
# CircuitPythonDHT - Reading temperature/humidity data from Adafruit DHT11 Sensor
# libgpiod2 - ???
# Board - Pin ids for DHT sensor
# adafruit-mcp3000 - Reading AC sensor readings

from sensor import *
from database import *
from control import *
from camera import *
from time import sleep

import board

##################
# INITIALIZATION #
##################
pumpRelay = Pump("GPIO25")
lampRelay = Lamp("GPIO24")
cameraControl = Camera()

#tempSensor = DHTSensor(board.D16)
lightSensor = MCPSensor(0)
moistureSensor = MCPSensor(1)

#####################
# MAIN PROGRAM LOOP #
#####################
mainLoopFlag = True
count = 0
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
    print("Light Sensor")
    print(lightSensor.read())
    print("Moisture Sensor")
    print(moistureSensor.read())
    ############
    # DATABASE #
    ############
    sleep(0.5)
    if (count < 10):
        count += 1
    else:
        mainLoopFlag = False
    
################
# TEST SECTION #
################

#print("Temperature")
#print(tempSensor.dhtDevice.temperature)
#test = tempSensor.dhtDevice.temperature
lampRelay.turnOn()
sleep(1)
lampRelay.turnOff()