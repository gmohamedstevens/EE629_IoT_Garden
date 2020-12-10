import board
import adafruit_dht

import gpiozero
from gpiozero import MCP3008

# Analog sensor attached to MCP3008 channel
class MCPSensor(object):
    # Object initialization
    def __init__(self, ch):
        self.channel = ch
        self.mcp = MCP3008(channel=ch)
    # Returns the reading of the sensor
    def read(self):
        #MCPSensor.mcp.read_adc(self.channel)
        return self.mcp.value
    # Return the GPIO pin the control is attached to
    def returnChannel(self):
        return self.channel
    # Set the GPIO pin the control is attached to
    def setChannel(self, ch):
        self.channel = ch
        self.mcp = MCP3008(channel=ch)

# DHT sensor manager
class DHTSensor(object):
    # Object initialization
    def __init__(self, pin):
        self.gpio_pin = pin
        self.dht_device = adafruit_dht.DHT22(pin)
    # Returns the temperature reading of the sensor
    def read_temperature(self):
        try:
            return self.dht_device.temperature
        except RuntimeError as error:
            print(error.args[0])
    # Returns the humidity reading of the sensor
    def read_humidity(self):
        try:
            return self.dht_device.humidity
        except RuntimeError as error:
            print(error.args[0])
    # Return the GPIO pin the control is attached to
    def return_gpio_pin(self):
        return self.gpio_pin
    # Set the GPIO pin the control is attached to
    def set_gpio_pin(self, pin):
        self.gpio_pin = pin
