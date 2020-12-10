import gpiozero

# Parent control class for relays
class Relay(object):
    # Object initialization
    def __init__(self, pin):
        self.gpio_pin = pin
        self.relay = gpiozero.OutputDevice(pin, active_high=False, initial_value=False)
    # Returns if control is on
    def is_on(self):
        return (self.relay.value == 1)
    # Returns if control is off
    def is_off(self):
        return not (self.relay.value == 1)
    # Turn off control
    def turn_off(self):
        self.relay.off()
    # Turn on control
    def turn_on(self):
        self.relay.on()
    # Return the GPIO pin the control is attached to
    def return_gpio_pin(self):
        return self.gpio_pin
    # Set the GPIO pin the control is attached to
    def set_gpio_pin(self, pin):
        self.gpio_pin = pin
        self.relay = gpiozero.OutputDevice(pin, active_high=False, initial_value=False)

# Relay-controlled water pump
class Pump(Relay):
    # Object initialization
    def __init__(self, pin):
        Relay.__init__(self, pin)

# Relay-controlled lamp
class Lamp(Relay):
    # Object initialization
    def __init__(self, pin):
        Relay.__init__(self, pin)