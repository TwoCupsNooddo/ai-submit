#!/usr/bin/env python
from __future__ import print_function
import rospy
from your_package.srv import Location , Nav
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import *

def go_to_location_client(self):
    rospy.init_node('go_to_location')
    rospy.wait_for_service('robot_following')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            robot_following = rospy.ServiceProxy('robot_following', Nav)
            print("input location")
            resp1 = robot_following(self.x)
            print(resp1)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)


def write_csv_client(self):
    rospy.init_node('write_csv')
    rospy.wait_for_service('robot_write')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            x = 10
            robot_write = rospy.ServiceProxy('robot_write', Location)
            print("input distances")
            resp2 = robot_write(x)
            print(resp2)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)


if __name__ == "__main__":
    write_csv_client(1)
