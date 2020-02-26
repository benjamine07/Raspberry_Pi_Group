#!/usr/bin/env python
# ROS only supports python 2!
#------------------------------------------------------------------------+
# run this with rosrun PACKAGENAME EXECUTABLE                            |
# where PACKAGENAME is the name of the ros package this file is in       |
# and EXECUTABLE is the name of this file                                |
#------------------------------------------------------------------------+

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
        steering_pos = 0.00 # placeholder data. Should come from game controller
        throttle_pos = 0.00 # placeholder data. Should come from game controller
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
