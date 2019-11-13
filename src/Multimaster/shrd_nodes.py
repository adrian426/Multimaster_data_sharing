import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Pose2D

class MasterCommunication(object):
    def __init__(self):
        rospy.init_node('local_topic_reader', log_level=rospy.DEBUG)