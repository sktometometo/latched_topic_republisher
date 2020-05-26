#!/usr/bin/env python

import argparse
import rospy
import rosbag
import geometry_msgs.msg
import tf2_ros
import tf2_msgs.msg
import sys
import importlib
import pydoc

def main():

    rospy.init_node( 'latched_topic_republisher' )

    topicname = rospy.get_param('~topicname','/tf_static')
    bagfilename = rospy.get_param("~file")

    module = None
    datatype = None

    with rosbag.Bag( bagfilename, 'r' ) as inputbag:
        try:
            topic, msg, t = inputbag.read_messages( topicname ).next()
        except:
            rospy.logerror( 'Cannot find any message with topic {}.'.format( topicname ) )
            sys.exit(1)
        packagename, typename = msg._type.split('/')
        print('from {}.msg import {}'.format(packagename,typename))
        module = importlib.import_module('{}.msg'.format(packagename))
        datatype = pydoc.locate('{}.msg.{}'.format(packagename,typename))

    publisher = rospy.Publisher(topicname, datatype, latch=True, queue_size=10)

    list_messages = []
    with rosbag.Bag( bagfilename, 'r' ) as inputbag:
        for topic, msg, t in inputbag.read_messages( topicname ):
            list_messages.append(msg)

    for message in list_messages:
        publisher.publish( message )

    rospy.loginfo( 'Republishing topic \'{}\''.format(topicname) )
    rospy.spin()

if __name__=='__main__':
    main()
