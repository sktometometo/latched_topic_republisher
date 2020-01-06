# static_tf_republisher

Rosbag play does not imitate latched topic functions such as /tf_static.
This package provides a node that republish latched /tf_static topic from a rosbag file.

## Usage

```
rosrun static_tf_republisher static_tf_republisher.py _file:=<your rosbag file>
```
