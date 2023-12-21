from pymycobot.mycobot import MyCobot
import pymycobot
from pymycobot import PI_PORT, PI_BAUD
import time
import os
import sys
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import time


mc = MyCobot("COM18",115200)
time.sleep (1)

mc.set_gripper_value(100,50)
mc.release_all_servos()
while True:
    a=mc.get_coords()
    print(a)