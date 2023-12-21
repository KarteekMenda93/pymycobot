# pymycobot

Perform homogenous transformation for the robot. And at last, Measure the length of the robot joints and verify them. (Refer to the datasheet for accurate measurements)
Handwrite the word “CIM”

Robotic arms are excellent for performing pick and place operations such as placing small electronic components on circuit boards, as well as large boxes on pallets. A pick-and-place operation will require at least 5 points

Home 
Above the pick point 
At the pick-point
Above the pick point
Above the place point
At the drop point
Above the place point
Home


As a rule, always go to a position above the pick or place point first so that the robot can accurately and repeatedly place the object straight down in a linear motion, with no friction or interference.

After the gripper is attached (you may use a suction pump or claw grabber). Place one of the wooden cups in front of the robot. (You may also use suction, refer to lab 3)
Now by using get_coords or get_angles, set_gripper_value, send_coords or send_angle try to pick up the block and place it further from the robot.


A pick-and-place style of moving objects around is a staple of industrial robots. Another reason to use robots in industry and automation is because of the danger to humans. Robots can work in adverse environments that are dangerous to humans; especially when dealing with chemicals and other toxic substances. 
A pick-and-place style of moving objects around is the staple of industrial robots. Another reason to use robots in industry and automation is because of the danger to humans. Robots can work in adverse environments that are dangerous to humans; especially when dealing with chemicals and other toxic substances. 

AI Kit(Artificial Intelligence Kit) 2023, an upgraded version of AI Kit. AI Kit 2023 is an entry-level AI Kit that combines visual, positioning, grabbing, and automatic sorting modules. The kit is based on the Python platform. It helps users who are just starting to learn the basics of AI and inspires them to think innovatively and understand the creative culture of open source.

AI Kit 2023 is a robotic arm application, simulating an industrial scenario. In this simulated industrial scenario, the robotic arm will replace manual labor to achieve smart sorting and implement preliminary industrial automation.

The 5 vision algorithms are：

● Shape recognition

● Feature point recognition

● ArUco code recognition

● Color recognition

● YOLOv5 recognition

This case uses the eye-to-hand mode, uses the camera, combines Python+OpenCV, performs color positioning through OpenCV, and frames the color blocks that meet the situation, and calculates the relative position of the blocks through the relevant points. at the spatial coordinate position of the manipulator. Set up a set of related actions for the robotic arm, and place them in different areas according to the color of the identified objects


This case uses the eye-to-hand mode, uses the camera to take pictures, loads the yolov5 model data through OpenCV, recognizes the image block and locates the position of the image block in the recognition area. Through the relevant points, the space coordinate position of the block relative to the robot arm is calculated. Set a set of related actions for the robot arm, and put the recognized object into the corresponding area.

Supported end effectors: myCobot Pro Single Head Suction Pump.
