from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='robot_core', executable='publisher', name='status_publisher'),
        Node(package='robot_core', executable='subscriber', name='status_subscriber')
    ])
