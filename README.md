# static_tf_republisher

`rosbag play` does not imitate latched topic functions such as /tf_static.
This package provides a node that republish /tf_static as a latched topic from a rosbag file.

## Usage

```
rosrun static_tf_republisher static_tf_republisher.py _file:=<your rosbag file>
```
