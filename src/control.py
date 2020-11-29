import gpiozero

# Parent control class for relays
class Relay:
    # Object initialization
    def __init__(self, pin):
        self.gpioPin = pin
        self.relay = gpiozero.OutputDevice(pin, active_high=False, initial_value=False)
    # Returns if control is on
    def isOn(self):
        return (self.relay.value == 1)
    # Returns if control is off
    def isOff(self):
        return not (self.relay.value == 1)
    # Turn off control
    def turnOff(self):
        self.relay.off()
    # Turn on control
    def turnOn(self):
        self.relay.on()
    # Return the GPIO pin the control is attached to
    def returnGPIOPin(self):
        return self.gpioPin
    # Set the GPIO pin the control is attached to
    def setGPIOPin(self, pin):
        self.gpioPin = pin
        self.relay = gpiozero.OutputDevice(pin, active_high=False, initial_value=False)

class Pump(Relay):
    # Object initialization
    def __init__(self, pin):
        Relay.__init__(self, pin)

class Lamp(Relay):
    # Object initialization
    def __init__(self, pin):
        Relay.__init__(self, pin)