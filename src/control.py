class Pump:
    # Object initialization
    def __init__(self):
        self.pumpOnFlag = False
    # Returns if pump is on
    def pumpIsOn(self):
        return self.pumpOnFlag
    # Turn off the water pump
    def turnOffPump(self):
        self.pumpOnFlag = False
    # Turn on the water pump
    def turnOnPump(self):
        self.pumpOnFlag = True


class Lamp:
    # Object initialization
    def __init__(self):
        self.lampOnFlag = False
    # Retutns if lamps is on
    def lampIsOn(self):
        return self.lampOnFlag
    # Turn off the lamp
    def turnOffLamp(self):
        self.lampOnFlag = False
    # Turn on the lamp
    def turnOnLamp(self):
        self.lampOnFlag = True