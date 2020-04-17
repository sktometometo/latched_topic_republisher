# latched_topic_republisher

Rosbag play does not imitate latched topic functions such as /tf_static.
This package provides a node that republish latched topic from a rosbag file.

## Usage

```
rosrun static_tf_republisher static_tf_republisher.py _file:=<your rosbag file> _topic:=<latched topic name like /tf_static>
```
