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

####################
# IMPORT LIBRARIES #
####################
# Monitor functions libraries
from sensor import *
from database import *
from control import *
# Flask web server libraries
from flask_server import *
# Misc. librariries
from time import sleep
import board
import multiprocessing
import threading
import sys

##################
# INITIALIZATION #
##################
pump_relay = Pump("GPIO25")
lamp_relay = Lamp("GPIO24")

light_sensor = MCPSensor(0)
moisture_sensor = MCPSensor(1)
sensor = MCPSensor(0)

app = Flask(__name__)
server = FlaskServer()

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
process_sensors = multiprocessing.Process(target=sensors)      

def flask_server():
    server.app.run(host='0.0.0.0',port='5000', debug=True, use_reloader=False)
process_flask = multiprocessing.Process(target=flask_server)

def start_processes():
    # start sensor processes
    process_sensors.start()
    print("Sensor process started.")        
    # start flask process
    process_flask.start()
    print("Flask process started.")
    
def end_processes():
    # terminate sensor process
    process_sensors.terminate()
    process_sensors.join()
    print("Sensor process ended.")
    sleep(1)
    # terminate flask process
    process_flask.terminate()
    process_flask.join()
    print("Flask process ended.")
    sleep(1)

#####################
# MAIN PROGRAM LOOP #
#####################
if __name__ == '__main__':
    print(__name__)
    lamp_relay.turn_on()
    sleep(1)
    lamp_relay.turn_off()
    try:
        start_processes() 
        # loop until keyboard interrupt is thrown
        main_loop_flag = True
        while main_loop_flag:
            pass
    except KeyboardInterrupt: 
        end_processes()
        # exit program
        print("Exiting program.")
        sleep(1)
        sys.exit(0)

