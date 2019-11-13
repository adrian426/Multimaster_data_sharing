#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
import math
import tf
import tf2_ros
import socket

from nav_msgs.msg import Odometry

from multimaster_shared_topics.msg import data
from std_msgs.msg import String

class MasterCommunicationNode(object):
    def __init__(self):
        self.hostname = socket.gethostname()
        rospy.init_node(self.hostname + '_local_topic_reader', log_level=rospy.DEBUG)
        self.odom = rospy.Subscriber('odom', Odometry, self.odom_callback)
        self.share_data_pub = rospy.Publisher(self.hostname + '/master_data', data, queue_size=5)
    
    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        quat = np.array([msg.pose.pose.orientation.x,
                            msg.pose.pose.orientation.y,
                            msg.pose.pose.orientation.z,
                            msg.pose.pose.orientation.w], np.float64)

        roll, pitch, yaw = tf.transformations.euler_from_quaternion(quat)
        #theta = yaw
        rospy.logdebug_throttle(1, "Received Odom msg (x, y, cita): %.2f, %.2f, %.2f" % (x, y, yaw))
    
    def pub_data(self):
        msg = data()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 'shared_data'
        msg.msg1 = self.hostname + 'gol'
        self.share_data_pub.publish(msg)

    def run(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub_data()



def main():
    node = MasterCommunicationNode()
    node.run()

if __name__ == '__main__':
    main()