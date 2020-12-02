# IoT Garden Monitor
# by Gamal Mohamed
#
# LIBRARIES USED:
# GPIOZero - Control of GPIO pins for sensors, lamp, pump, etc. and reading MCP3008 channels
# CircuitPythonDHT - Reading temperature/humidity data from Adafruit DHT11 Sensor
# Board - Pin ids for DHT sensor
# Multiprocessing - for running multple processes (sensing, web server, image capture)
# Pygame.camera - image capture through OpenCV

from sensor import *
from database import *
from control import *
#from camera import *


from flask_server import *
from flask import Flask, render_template, Response
#import camera_opencv
#from camera_opencv import VideoCamera


from time import sleep
import board
import multiprocessing

##################
# INITIALIZATION #
##################
pump_relay = Pump("GPIO25")
lamp_relay = Lamp("GPIO24")
#camera_control = Camera()

#tempSensor = DHTSensor(board.D16)
light_sensor = MCPSensor(0)
moisture_sensor = MCPSensor(1)
sensor = MCPSensor(0)

app = Flask(__name__)

#############
# PROCESSES #
#############
def sensors():
    #while True:
        #print("Light Sensor")
        #print(light_sensor.read())
        #print("Moisture Sensor")
        #print(moisture_sensor.read())
        #sleep(1)
    pass
        
def flask_server():
    server = FlaskServer()
    server.app.run(host='0.0.0.0',port='5000', debug=True)

def test():
    while True:
        print("Hello :)")
        sleep(0.5)
    
process_sensors = multiprocessing.Process(target=sensors) 
process_sensors.start()

process_flask = multiprocessing.Process(target=flask_server) 
process_flask.start()

#####################
# MAIN PROGRAM LOOP #
#####################
main_loop_flag = True
count = 0
while(main_loop_flag):
    ##########
    # CAMERA #
    ##########
    #photo = cameraControl.takePhoto()
    #cameraControl.addToTimeLapse(photo)
    #cameraControl.updateLiveFeed(photo)
    ##########
    # SENSOR #
    ##########
    #print("Light Sensor")
    #print(lightSensor.read())
    #print("Moisture Sensor")
    #print(moistureSensor.read())
    ############
    # DATABASE #
    ############
    sleep(1)
    if (count < 15):
        count += 1
    else:
        main_loop_flag = False
    
################
# TEST SECTION #
################


#print("Temperature")
#print(tempSensor.dhtDevice.temperature)
#test = tempSensor.dhtDevice.temperature
lamp_relay.turn_on()
sleep(1)
lamp_relay.turn_off()

#camera_control.start_cam()
#image = camera_control.take_photo()
#camera_control.save_photo(image, 'img/picture.jpg')
#camera_control.stop_cam()

#################
# END PROCESSES #
#################
process_sensors.join()
process_sensors.terminate()

process_flask.join()
process_flask.terminate()
