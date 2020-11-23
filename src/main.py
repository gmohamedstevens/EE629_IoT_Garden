import sensor
import database
from control import *

pumpControl = Pump()
lampControl = Lamp()



if lampControl.lampIsOn():
    print("Lamp is on")
else:
    print("Lamp is off")



lampControl.turnOnLamp()
if lampControl.lampIsOn():
    print("Lamp is on")
else:
    print("Lamp is off")