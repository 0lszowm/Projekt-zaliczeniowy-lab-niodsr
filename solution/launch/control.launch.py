
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim_node',
            emulate_tty=True,
        ),
        Node(
            package='solution',
            executable='control',
            name='control_node',
            emulate_tty=True,
            output='screen',
        ),
    ])