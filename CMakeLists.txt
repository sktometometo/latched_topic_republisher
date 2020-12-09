cmake_minimum_required(VERSION 2.8.3)
project(static_tf_republisher)

find_package(catkin REQUIRED)

catkin_package(
)

include_directories(
)

install(PROGRAMS
    node_scripts/static_tf_republisher.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
