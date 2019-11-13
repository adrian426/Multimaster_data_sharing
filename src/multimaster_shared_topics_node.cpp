#include <ros/ros.h>
#include "std_msgs/String.h"
#include <iostream>
#include <stdlib.h>
#include <unistd.h>
using namespace std;

void chatter_callback(const std_msgs::String::ConstPtr& msg){
    ROS_INFO("nAn");
}

//Mejor hacerlo en python: http://cerlab.ucr.ac.cr/git/danidim13/vfhp_ros/src/master/vfhp_local_planner/scripts/vfhp_node.py
int main(int argc, char** argv){
    ros::init(argc, argv, "shared_topics_node");
    ros::NodeHandle n("~");
    ros::Rate loop_rate(50);
    ros::Subscriber odom = n.subscribe("odom", 1000, chatter_callback);
    while(ros::ok()){
        ros::spinOnce();

        loop_rate.sleep();
    }
}