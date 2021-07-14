#!/usr/bin/env python3

import rospy
import sys
from geometry_msgs.msg import Twist

def move_circle():
	rospy.init_node('simbot_move_circle', anonymous=True)

	vel_pub = rospy.Publisher(
		'/simbot/base_controller/cmd_vel', Twist, queue_size=10
	)
	
	msg = Twist()
	msg.linear.x = 0.1
	msg.linear.y = 0
	msg.linear.z = 0
	msg.angular.x = 0
	msg.angular.y = 0
	msg.angular.z = 0.08

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		vel_pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		move_circle()
	except rospy.ROSInterruptException:
		pass
