# Import the necessary libraries
from pymycobot.mycobot import MyCobot
import time

# Initiating the library by letting the cobot to connect from the mentioned port serial port and baud rate
mc = MyCobot("COM17", 115200)# Create object

# Return the robotic arm to zero
mc.send_angles([0, 90, -60, 0, 0, 20], 50)# First, set all positions of the motors to 0 degrees
#time.sleep(2)# A time delay of 5 seconds
#mc.set_gripper_value(50, 50)# open the gripper halfway
#time.sleep(5)# A time delay of 5 seconds
mc.release_all_servos()# releasing the motors

# Starting an infinite loop to extract and print the angles of the motors of the cobot.
i = 1
while i == 1:
    print("::get_coords() ==> coords: {}\n".format(mc.get_coords()))
    time.sleep(3)

mc.release_all_servos()