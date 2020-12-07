### EE629 IoT Garden Monitor
###### By Gamal Mohamed

**Project:** IoT Garden Monitor

**Description:** An automated plant monitoring system. Functions include sensing and reporting plant metrics, water pump and lamp control, and webcam streaming

#########################

**Weekly Update 2020-12-07:**

Accomplishments for this week:
- USB camera video capture implemented through OpenCV
- Test Flask server running and live video feed operational
- Running sensor collection and Flask server on separate processes for multitasking
- Restructured main program loop to be more organized and exit gracefully
In development for next week:
- Update Flask template to be more user friendly and provide more data
- Database connections and management through SQLite
- Automated controls based on plant metrics

References for Flask and video streaming:
- https://projects.raspberrypi.org/en/projects/python-web-server-with-flask
- https://stackoverflow.com/questions/35616639/python-multiprocessing-in-flask
References for threading and multiprocessing libraries
- https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
- https://cuyu.github.io/python/2016/08/15/Terminate-multiprocess-in-Python-correctly-and-gracefully
- https://stackoverflow.com/questions/39258616/running-two-process-simultaneously
- https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python

#########################

**Weekly Update 2020-11-29:**

Since last week, the garden monitor is capable of monitoring the AC sensor input using an MCP3008 ADC converter. Also, I've used the GPIO Zero library to control the lamp and water pump through the GPIO pins.

The goal for next week is to have the following tasks complete:
- USB camera access through OpenCV - provide live feed to web app and time lapse functionality
- Sensor and image database through SQLite - libraries have been imported
- Web access through Flask - allows for monitoring plant metrics (historical and current) and manually controlling lamp/water pump
- Threading - use 'threading' library to separate web access functions from sensing/control functions

References for GPIO configuration:
- https://pinout.xyz/pinout/pin10_gpio15# - Raspberry Pi Pin Map
- https://gpiozero.readthedocs.io/en/stable/recipes.html - MCP3008 GPIO Zero Configuration

#########################

**Weekly Update 2020-11-23:**

I've restructured the original functionality test code and began building the class structure to read and control the modules. Also, I've begun pushing source code to GitHub.

Classes started:
- Camera - Controls webcam input and photo capture; for time-lapse
- Sensor - Grabs sensor data; can be passed to database or help automate pump/lamp functions
- Control - Handles automated and manual control of lamp and water pump
Database - Collects data into database; for forwarding to user app

#########################

**Weekly Update 2020-11-15:**

For the next few weeks, I will be wrapping up mt IoT Garden Monitor project. Progress and planned work are as follows:

What I've already completed:
- General model and function of the system
- Material and parts gathered
- Software and programming libraries reviewed and gathered

My goals for completing this project:
- Sensor input monitoring
- Raspberry Pi/web app interactions
- Lamp and water pump control (manual and auto)


![IoT Garden Monitor Diagram](/img/iot-plant-monitor-diagram.png)