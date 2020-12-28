### EE629 IoT Garden Monitor
###### By Gamal Mohamed

**Project:** IoT Garden Monitor

**Description:** An automated plant monitoring system. Functions include sensing and reporting plant metrics, water pump and lamp control, and webcam streaming

![IoT Garden Monitor Diagram](/img/iot-plant-monitor-diagram.png)

**Flask and Live Feed Demonstration:** https://drive.google.com/file/d/1hJV7r7yVq3m-x4LE2NaX5lyJd88VJ5NO/view?usp=sharing

**Data Streaming Demonstration:** https://drive.google.com/file/d/1tHtQIWygJrrLxRBwUfoqpnsDXOxmyptb/view?usp=sharing

***

**Hardware Used:**
- Raspberry Pi 3 Model B [Amazon Link](https://www.amazon.com/gp/product/B01C6Q2GSY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
- Sensor kit [Amazon Link](https://www.amazon.com/gp/product/B01J9GD3DG/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1)
--In particular, the following parts are used:
---
---
---
- Standard breadboard and jumper wires for making electrical connections

**Python Libraries Used:**
- GPIO Zero - For controlling GPIO pins of the Raspberry Pi
- OpenCV - Accessing USB web camera for web page live feed and time lapse photo
- Multiprocessing - Multitasking the functions of the monitor (sensing, web server, webcam image capture)
- SQLite3 - Building a database for storing sensor data
- Flask - Hosted web server 

***
## Electrical Schematic
Section under construction

***