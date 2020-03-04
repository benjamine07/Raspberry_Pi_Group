#!/usr/bin/env python
# ROS only supports python 2!
#------------------------------------------------------------------------+
# run this with rosrun PACKAGENAME EXECUTABLE                            |
# where PACKAGENAME is the name of the ros package this file is in       |
# and EXECUTABLE is the name of this file                                |
#------------------------------------------------------------------------+
# racecar_data_sub.py

# This file should be run in a ROS package on a Raspberry Pi that is conected to the racecar
# It requires the a PiHat for PWM generation, see: https://github.com/lbaitemple/rpiHAT for details
# This code subscribes to a single ROS topic containing a len 2 array holding the PWM duty cycle
# that is output to the racecar servo and ESC

#-------------------------------------------------------------------------
# import necessary libraries for ros methods
import rospy
from std_msgs.msg import Float32MultiArray

# import libraries for PWM servo/ESC control
# https://github.com/lbaitemple/rpiHAT
from rpiHAT import ServoNT
import time
import sys

#-------------------------------------------------------------------------
# this is called when something we subscribed to is published
def callback(data):
    # log the data
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    # control the car, we expect published data to be in duty cycle in range [0.10, 0.20]
    if data.data[0] > 0.20:
        rospy.loginfo(rospy.get_caller_id() + '%s greater than maximum of 0.20, setting to max', data,data[0])
        steering.pulse(0.20)
    elif data.data[0] < 0.10:
        rospy.loginfo(rospy.get_caller_id() + '%s less than minimum of 0.10, setting to min', data,data[0])
        steering.pulse(0.10)
    else:
        steering.pulse(data.data[0])

    if data.data[1] > 0.20:
        rospy.loginfo(rospy.get_caller_id() + '%s greater than maximum of 0.20, setting to max', data,data[1])
        throttle.pulse(0.20)
    elif data.data[1] < 0.10:
        rospy.loginfo(rospy.get_caller_id() + '%s less than minimum of 0.10, setting to min', data,data[1])
        throttle.pulse(0.10)
    else:
        throttle.pulse(data.data[1])

#-------------------------------------------------------------------------
# this is the main function where subscriptions are setup
def racecar_data_sub():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our '' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('racecar_data_sub', anonymous=True)

    # set up subscriptions to each topic and callback funcs
    rospy.Subscriber('racecar/controller_data', Float32MultiArray, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

#-------------------------------------------------------------------------
# run this file if it is not imported as a library
if __name__ == '__main__':
    # setup PWM and initialize to neutral
    steering = ServoNT(channel=1, freq=92.7)
    throttle = ServoNT(channel=2, freq=92.7)
    steering.pulse(0.15)
    throttle.pulse(0.15)
    # subscribe to data and act accordingly 
    racecar_data_sub()
