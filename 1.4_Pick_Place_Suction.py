from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD
import time
import os
import sys
from pymycobot.genre import Angle,Coord
from pymycobot.genre import Angle,Coord
import time

mc = MyCobot("COM18", 115200)


# Turn on the suction pump, note: use one of pins 2 and 5 to control the switch of the suction pump
def pump_on():
    # Let bit 2 work
    mc.set_basic_output(2, 0)
    # Let bit 5 work
    #mc.set_basic_output(5, 0)

# Stop suction pump
def pump_off():
    # Make position 2 stop working
    mc.set_basic_output(2, 1)
    # Make position 5 stop working
    #mc.set_basic_output(5, 1)


mc.send_angles([0,0,0,0,0,0], 10)

time.sleep(2)

pump_on()

time.sleep(3)

mc.send_coords([-26.7, -111.8, 273.4, -178.53, -8.62, -131.81], 20, 0)      # above the pick point

time.sleep(3)

pump_off()

time.sleep(3)

mc.send_coords([-31.6, -199.0, 97.5, 178.17, 6.91, -139.02], 20, 0)        #at the pick point

time.sleep(3)

pump_on()

time.sleep(3)

mc.send_coords([-35.3, -191.3, 200.7, 177.47, 4.67, -138.89], 20, 0)        #above the pick point

time.sleep(3)

mc.send_coords([86.1, -154.0, 233.0, -178.51, 0.61, -91.65], 20, 0)        #above the place point

time.sleep(3)

mc.send_coords([112.2, -154.9, 114.0, 176.03, 4.62, -69.91], 20, 0)        #at the place point

time.sleep(3)

pump_off()

time.sleep(3)

mc.send_coords([92.4, -141.7, 195.1, -178.06, -0.32, -88.58], 20, 0)        #above the place point

time.sleep(3)



time.sleep(3)
