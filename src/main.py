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
from camera_opencv import VideoCamera

# Misc. librariries
from time import sleep
import board
import multiprocessing
import threading
import sys
import datetime

##################
# INITIALIZATION #
##################
# Control objects for controlling relays 
pump_relay = Pump("GPIO25")
lamp_relay = Lamp("GPIO24")

# Sensor objects for collecting sensor values
light_sensor = MCPSensor(0)
moisture_sensor = MCPSensor(1)

cam = VideoCamera()

# Flask server object for managing server requests
server = FlaskServer(cam)

# Database objects for collecting senosr and image data
database_manager = Database()
database_connection = database_manager.create_connection('db/data.db')
database_manager.initialize_tables(database_connection)


# database_manager.insert_light_sensor_data(database_connection, (str(datetime.datetime.now()), 1.0))
# database_manager.insert_moisture_sensor_data(database_connection, (str(datetime.datetime.now()), 1.0))
# database_manager.insert_image_data(database_connection, (str(datetime.datetime.now()), 1.0))


#############
# PROCESSES #
#############
# Process for capturing sensor data
def sensors():
    while True:
        sensor1 = light_sensor.read()
        sensor2 = moisture_sensor.read()
        print("Light Sensor")
        print(sensor1)
        print("Moisture Sensor")
        print(sensor2)
        # Write sensor data to database
        #database_manager.insert_light_sensor_data(database_connection, (str(datetime.datetime.now()), sensor1))
        #database_manager.insert_moisture_sensor_data(database_connection, (str(datetime.datetime.now()), sensor2))
        sleep(5)
process_sensors = multiprocessing.Process(target=sensors) 

# Process for managing Flask server requests
def flask_server():
    server.app.run(host='0.0.0.0',port='5000', debug=True, use_reloader=False)
process_flask = multiprocessing.Process(target=flask_server)

def video_stream():
    while True:
        cam.update_frame()
        cam.timelapse_photo()
        sleep(60)
process_video = multiprocessing.Process(target=video_stream)

# Start the proccesses of the garden monitor
def start_processes():
    # start video streaming process
    process_video.start()
    print("Video streaming process started.")    
    # start sensor processes
    process_sensors.start()
    print("Sensor process started.")        
    # start flask process
    process_flask.start()
    print("Flask process started.")
    
  
# End the processes of the garden monitor
def end_processes():
    # Terminate flask process
    process_flask.terminate()
    process_flask.join()
    print("Flask process ended.")
    # Terminate sensor process
    process_sensors.terminate()
    process_sensors.join()
    print("Sensor process ended.")
    # Terminate video streaming process
    process_video.terminate()
    process_video.join()
    print("Video streaming process ended.")

#####################
# MAIN PROGRAM LOOP #
#####################
if __name__ == '__main__':
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
        sys.exit(0)

