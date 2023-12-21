# This code is for setting up the arm with different angles and colors
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import time

mc = MyCobot("COM3", 115200)
mc.send_angles([0, 0, 0, 0, 0, 0], 50)
i = 2
while i > 0:
    mc.set_color(0, 0, 255)  # blue light on
    time.sleep(2)  # wait for 2 seconds
    mc.set_color(255, 0, 0)  # red light on
    time.sleep(2)  # wait for 2 seconds
    mc.set_color(0, 255, 0)  # green light on
    time.sleep(2)  # wait for 2 seconds
    i -= 1
mc.release_all_servos()