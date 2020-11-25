# Parent control class
class Control:
    # Object initialization
    def __init__(self, pin):
        self.GPIOPin = pin
        self.onFlag = False
    # Returns if control is on
    def isOn(self):
        return self.onFlag
    # Returns if control is off
    def isOff(self):
        return not self.onFlag
    # Turn off control
    def turnOff(self):
        self.onFlag = False
    # Turn on control
    def turnOn(self):
        self.onFlag = True
    # Return the GPIO pin the control is attached to
    def returnGPIOPin(self):
        return self.GPIOPin
    # Set the GPIO pin the control is attached to
    def setGPIOPin(self, pin):
        self.GPIOPin = pin

class Pump(Control):
    # Object initialization
    def __init__(self, pin):
        Control.__init__(self, pin)

class Lamp(Control):
    # Object initialization
    def __init__(self, pin):
        Control.__init__(self, pin)