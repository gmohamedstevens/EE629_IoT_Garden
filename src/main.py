# IoT Garden Monitor
# by Gamal Mohamed
#
# LIBRARIES USED:
# GPIO Zero - Control of GPIO pins for sensors, lamp, pump, etc. and reading MCP3008 channels
# CircuitPythonDHT - Reading temperature/humidity data from Adafruit DHT11 Sensor
# Board - Pin IDs for DHT sensor
# Multiprocessing, threading - for running multitasking (sensing, web server, image capture)
# Flask - Web server and network access
# OpenCV - Image capture from USB web cam
# SQLite3 - For building databases to store sensor data and timelapse photos
# DateTime - For timed control actions and live feed time stamps

####################
# IMPORT LIBRARIES #
####################
# Monitor function libraries
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
# Control objects for controlling relays 
pump_relay = Pump("GPIO25")
lamp_relay = Lamp("GPIO24")

# Sensor objects for collecting sensor values
light_sensor = MCPSensor(0)
moisture_sensor = MCPSensor(1)
sensor = MCPSensor(0)

# Flask server object for managing server requests
server = FlaskServer()

# Database objects for collecting senosr and image data
sensor_database = Database()
sensor_database.create_connection('db/sensor_data.db')

#############
# PROCESSES #
#############
# Process for capturing sensor data
def sensors():
    while True:
        print("Light Sensor")
        print(light_sensor.read())
        print("Moisture Sensor")
        print(moisture_sensor.read())
        sleep(5)
process_sensors = multiprocessing.Process(target=sensors)      

# Process for managing Flask server requests
def flask_server():
    server.app.run(host='0.0.0.0',port='5000', debug=True, use_reloader=False)
process_flask = multiprocessing.Process(target=flask_server)

# Start the proccesses of the garden monitor
def start_processes():
    # start sensor processes
    process_sensors.start()
    print("Sensor process started.")        
    # start flask process
    process_flask.start()
    print("Flask process started.")
  
# End the processes of the garden monitor
def end_processes():
    # Terminate sensor process
    process_sensors.terminate()
    process_sensors.join()
    print("Sensor process ended.")
    sleep(1)
    # Terminate flask process
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
        # Loop until keyboard interrupt is thrown
        main_loop_flag = True
        while main_loop_flag:
            pass
    # Graceful exit on keyboard interrupt
    except KeyboardInterrupt: 
        print()
        end_processes()
        # Exit program
        print("Exiting program.")
        sleep(1)
        sys.exit(0)

