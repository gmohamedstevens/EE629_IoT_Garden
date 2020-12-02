# IoT Garden Monitor
# by Gamal Mohamed
#
# LIBRARIES USED:
# GPIOZero - Control of GPIO pins for sensors, lamp, pump, etc. and reading MCP3008 channels
# CircuitPythonDHT - Reading temperature/humidity data from Adafruit DHT11 Sensor
# Board - Pin ids for DHT sensor
# Multiprocessing, threading - for running multitasking (sensing, web server, image capture)
# Flask - Web server and network access
# OpenCV - image capture from USB web cam

# Monitor functions libraries
from sensor import *
from database import *
from control import *
# Flask web server libraries
from flask_server import *
from flask import Flask, render_template, Response
# Misc. librariries
from time import sleep
import board
import multiprocessing
import threading
import sys
import os

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
    while True:
        print("Light Sensor")
        print(light_sensor.read())
        print("Moisture Sensor")
        print(moisture_sensor.read())
        sleep(5)
       
server = FlaskServer()
def flask_server():
    server.app.run(host='0.0.0.0',port='5000', debug=True, use_reloader=False)

def test():
    while True:
        print("Hello :)")
        sleep(0.5)

def main():
    # Sensor data gathering process
    process_sensors.start()

def end_processes():
    process_sensors.terminate()
    process_sensors.join()

    process_flask.terminate()
    process_flask.join()

#####################
# MAIN PROGRAM LOOP #
#####################
if __name__ == '__main__':
    print(__name__)
    lamp_relay.turn_on()
    sleep(1)
    lamp_relay.turn_off()
    try:
        # start sensor processes
        process_sensors = multiprocessing.Process(target=sensors)
        process_sensors.start()
        print("sensors started")        
        # start flask process
        process_flask = multiprocessing.Process(target=flask_server)
        process_flask.start()
        # loop until keyboard interrupt is thrown
        main_loop_flag = True
        while main_loop_flag:
            print("Hello :)")
            sleep(0.5)
            pass
    except KeyboardInterrupt: 
        # terminate sensor process
        process_sensors.terminate()
        process_sensors.join()
        print("sensors ended")
        # terminate flask process
        process_flask.terminate()
        process_flask.join()
        print("flask ended")
        # exit program
        print("Exiting program...")
        sys.exit(0)

