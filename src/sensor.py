import board
import adafruit_dht

class ACSensor:
        # Object initialization
        def __init__(self, pin, channel):
                self.GPIOPin = pin
                self.channel = channel
        # Returns the reading of the sensor
        def read(self):
                pass
        # Return the GPIO pin the control is attached to
        def returnGPIOPin(self):
                return self.GPIOPin
        # Set the GPIO pin the control is attached to
        def setGPIOPin(self, pin):
                self.GPIOPin = pin
                
class DHTSensor:
        # Object initialization
        def __init__(self, pin):
                self.GPIOPin = pin
                self.dhtDevice = adafruit_dht.DHT22(pin)
        # Returns the temperature reading of the sensor
        def readTemperature(self):
            try:
                return self.dhtDevice.temperature
            except RuntimeError as error:
                print(error.args[0])
        # Returns the humidity reading of the sensor
        def readHumidity(self):
            try:
                return self.dhtDevice.humidity
            except RuntimeError as error:
                print(error.args[0])
        # Return the GPIO pin the control is attached to
        def returnGPIOPin(self):
                return self.GPIOPin
        # Set the GPIO pin the control is attached to
        def setGPIOPin(self, pin):
                self.GPIOPin = pin