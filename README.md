### EE629 IoT Garden Monitor
###### By Gamal Mohamed

**Project:** IoT Garden Monitor

**Description:** An automated plant monitoring system. Functions include sensing and reporting plant metrics, water pump and lamp control, and webcam streaming

![IoT Garden Monitor Diagram](/img/iot-plant-monitor-diagram.png)

**Flask and Live Feed Demonstration:** https://drive.google.com/file/d/1hJV7r7yVq3m-x4LE2NaX5lyJd88VJ5NO/view?usp=sharing

**Data Streaming Demonstration:** https://drive.google.com/file/d/1tHtQIWygJrrLxRBwUfoqpnsDXOxmyptb/view?usp=sharing

***
#### Requirements
**Hardware Used:**
- Raspberry Pi 3 Model B [Amazon Link](https://www.amazon.com/gp/product/B01C6Q2GSY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- Sensor kit [Amazon Link](https://www.amazon.com/gp/product/B01J9GD3DG/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1)
	-In particular, the following parts are used:
		-
		-
		- MCP3008 Analog to Digital Converter
- Standard breadboard and jumper wires for making electrical connections
- Relay modules
- USB webcam 
- Full spectrum, LED grow light bulb [Amazon Link](https://www.amazon.com/gp/product/B07NN6SVG6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- AC house lamp
- Plant housing, dirt, seeds [Amazon Link](https://www.amazon.com/Educational-Insights-Sprout-Grow-Window/dp/B000066CMG)

**Python Libraries Used:**
- GPIO Zero - For controlling GPIO pins of the Raspberry Pi and reading analog sensors attached to MCP3008 sensor
- OpenCV - Accessing USB web camera for web page live feed and time lapse photo
- Multiprocessing - Multitasking the functions of the monitor (sensing, web server, webcam image capture)
- SQLite3 - Building a database for storing sensor data
- Flask - Simple web server hosting on Raspberry Pi
- DateTime - Handling timed control actions and adding time stamp to live feed

***
#### Electrical Schematic
Section under construction

***
