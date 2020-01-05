#!/usr/bin/env python

import argparse
import rospy
import rosbag
import geometry_msgs.msg
import tf2_ros
import tf2_msgs.msg
import sys

def main():
    rospy.init_node("static_tf_republisher")

    publisher = rospy.Publisher('tf_static', tf2_msgs.msg.TFMessage, latch=True, queue_size=10)
    bagfilename = rospy.get_param("~file")

    list_transform = []
    with rosbag.Bag( bagfilename, 'r' ) as inputbag:
        transform = geometry_msgs.msg.TransformStamped()
        for topic, msg, t in inputbag.read_messages('/tf_static'):
            list_transform += msg.transforms

    for transform in list_transform:
        transform.header.stamp = rospy.Time.now()
    pubmsg = tf2_msgs.msg.TFMessage()
    pubmsg.transforms = list_transform
    publisher.publish(pubmsg)

    rospy.loginfo( 'republishing static tf' )
    rospy.spin()

if __name__=='__main__':
    main()
