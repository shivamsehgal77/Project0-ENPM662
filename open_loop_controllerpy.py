#! /usr/bin/env python

#imported libraries
import rospy
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

#rospy to make the node as speed_controller
rospy.init_node("speed_controller")


#publishers
pub=rospy.Publisher("cmd_vel", Twist,queue_size=1)
#odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)


#Enter desired input of distance.
print("Enter the distane to which the robot should move =")
goal=float(input())

#Enter desired input of time.
print("Enter the time for which the robot should run = ")
t=float(input())


t_end=time.time() + t
#position=Odometry()
#x_current = position.pose.pose.position.x


speed= Twist()
speed.linear.x = 0.0
speed.linear.y = 0.0
speed.linear.z = 0.0
speed.angular.x = 0.0
speed.angular.y = 0.0
speed.angular.z = 0.0



rate_1= rospy.Rate(1)


speed.linear.x=goal/t



while time.time()< t_end:  
    speed.linear.y = 0.0
    speed.linear.z = 0.0
    speed.angular.x = 0.0
    speed.angular.y = 0.0
    speed.angular.z = 0.0
        

    pub.publish(speed)
    #pub.publish(position)
    rate_1.sleep()

speed.linear.x=0.0
pub.publish(speed)


