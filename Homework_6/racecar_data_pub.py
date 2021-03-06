#!/usr/bin/env python
# ROS only supports python 2!
#------------------------------------------------------------------------+
# run this with rosrun PACKAGENAME EXECUTABLE                            |
# where PACKAGENAME is the name of the ros package this file is in       |
# and EXECUTABLE is the name of this file                                |
#------------------------------------------------------------------------+
# racecar_data_pub.py

# This file should be run in a ROS package on a Raspberry Pi with a USB game controller attached
# This code publishes to a single ROS topic containing a len 2 array holding the PWM duty cycle
# that is obtained from the game controller. In this way we are able to read controller data
# and send it to another Raspberry Pi to controll the racecar. Both Pis are required to have a
# network connection to each other

#-------------------------------------------------------------------------
# import necessary libraries for ros methods
from std_msgs.msg import Float32MultiArray

#-------------------------------------------------------------------------
# this is the main function where publications are setup
def racecar_data_pub():
    # init objects to publish with ros
    pub_topic = rospy.Publisher('racecar/controller_data', Float32MultiArray, queue_size=10)

    # init ros node
    rospy.init_node('racecar_data_pub', anonymous=True)
    rate = rospy.Rate(20) # 20hz

    # loop forever and publish payloads
    while not rospy.is_shutdown():
        # data.axes should come from the game controller and be in range [-1.0, 1.0]
        steering_pos = abs(0.05*data.axes[0]-0.15)
        throttle_pos = 0.05*data.axes[1]+0.15
        racecar_data = [steering_pos, throttle_pos]
        # publish topic
        rospy.loginfo(racecar_data)
        pub_topic.publish(racecar_data)
    
        # sleep a bit so we don't spam publications
        rate.sleep()

#-------------------------------------------------------------------------
# run this file if it is not imported as a library
if __name__ == '__main__':
    try:
        racecar_data_pub()
    except rospy.ROSInterruptException:
        pass
