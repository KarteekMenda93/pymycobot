from pymycobot import MyCobot
import time

mc = MyCobot("COM3",115200)

for i in range(1,7):
    mc.set_servo_calibration(i)
    time.sleep(0.5)

mc.release_all_servos()