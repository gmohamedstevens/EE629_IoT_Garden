### EE629 IoT Garden Monitor
###### By Gamal Mohamed

**Description:** An automated plant monitoring system. Functions include sensing and reporting plant metrics, water pump and lamp control, and webcam streaming

![IoT Garden Monitor Diagram](/img/iot-plant-monitor-diagram.png)

**Flask and Live Feed Demonstration:** https://drive.google.com/file/d/1hJV7r7yVq3m-x4LE2NaX5lyJd88VJ5NO/view?usp=sharing

**Data Streaming Demonstration:** https://drive.google.com/file/d/1tHtQIWygJrrLxRBwUfoqpnsDXOxmyptb/view?usp=sharing

***
#### Hardware
- Raspberry Pi 3 Model B - [Amazon Link](https://www.amazon.com/gp/product/B01C6Q2GSY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- Sensor kit - [Amazon Link](https://www.amazon.com/gp/product/B01J9GD3DG/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1)
	- In particular, the following parts are used:
		- 5V 2-Channel Relay Module
		- Photosensitive Sensor Module
		- MCP3008 Analog to Digital Converter
- Automatic Irrigation Kit - [Amazon Link](https://www.amazon.com/WayinTop-Automatic-Irrigation-Watering-Capacitive/dp/B07TLRYGT1/ref=sr_1_3?dchild=1&keywords=automatic+irrigation+diy&qid=1611628170&sr=8-3)
	- Capacitive Soil Moisture Sensor
	- 5V DC Water Pump
	- Vinyl Tubing
- USB webcam (any should do, I used a Logitech C270)
- Full spectrum, LED grow light bulb - [Amazon Link](https://www.amazon.com/gp/product/B07NN6SVG6/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- AC power lamp (any will do, as long as grow light bulb fits it)
- Plant housing, dirt, seeds - [Amazon Link](https://www.amazon.com/Educational-Insights-Sprout-Grow-Window/dp/B000066CMG)
- Standard breadboard and jumper wires for making electrical connections

***
#### Python Dependencies & Libraries
- *GPIO Zero* - For controlling GPIO pins of the Raspberry Pi and reading analog sensors attached to MCP3008 sensor
- *OpenCV* - Accessing USB web camera for web page live feed and time lapse photo
- *Multiprocessing* - Multitasking the functions of the monitor (sensing, web server, webcam image capture)
- *SQLite3* - Building a database for storing sensor data
- *Flask* - Simple web server hosting on Raspberry Pi
- *DateTime* - Handling timed control actions and adding time stamp to live feed

***
#### Electrical Schematic
Section under construction

***
