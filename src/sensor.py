import board

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
    def return_channel(self):
        return self.channel
    # Set the GPIO pin the control is attached to
    def set_channel(self, ch):
        self.channel = ch
        self.mcp = MCP3008(channel=ch)

    #
    def return_percentage(self, sensor_min, sensor_max, decimal_places):
        if sensor_max < sensor_min:
            percent = (sensor_min - self.read())/(sensor_min - sensor_max) * 100.0
        else:
            percent = (self.read() - sensor_min)/(sensor_max - sensor_min) * 100.0
        return format(percent, '.' + str(decimal_places) + 'f') + '%'
        
