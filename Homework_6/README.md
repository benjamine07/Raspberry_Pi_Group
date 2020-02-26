# Assignment Overview
Homework 6 involves the creation of Robotic Operating System (ROS) nodes with the end goal of controlling an RC racecar and recording data from the vehicle. The key tasks are:
- Create three ROS nodes to communicate with each other of the same LAN
  1. R Pi 1 (standalone): connect a USB gamepad/controller and publish button/joystick data with a ROS node
  2. R Pi 2 (attatched to racecar): create a second ROS node that subscribes to button/joystick data and creates a corresponding PWM signals to control racecar throttle and steering. This should also *publish* data from the attached camera.
  3. Ubuntu VM: the third ROS node subscribes to all published data from the car and controller nodes, acting as a data logger. 
    - throttle and steering should be saved as a CSV via pandas library (python)
- Convert this README.md into a PDF to be submitted
- Document the assignment in a GitHub Repo

### Notes About the Racecar Setup
The Racecar is a Traxxas 4WD RC car. The motor ESC and steering servo are controlled by an ob-board Raspberry Pi 3b (R Pi). The R Pi generates the PWM signals needed byt he ESC and servo via a hardware module that communicates with the R Pi via I2C.
The software is several ROS nodes used for development of the vehicle control software. 