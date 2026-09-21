import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue 

def generate_launch_description():
    vid = LaunchConfiguration("vid")
    pid = LaunchConfiguration("pid")

    declare_vid = DeclareLaunchArgument(
        "vid",
        default_value="16d0",
        description="USB vendor ID of the chassis serial port",
    )
    declare_pid = DeclareLaunchArgument(
        "pid",
        default_value="1492",
        description="USB product ID of the chassis serial port",
    )

    serial_driver_node = Node(
        package='ros2_libxr',
        executable='ros2_libxr_node',
        name='rm_serial_driver',
        output='both',
        emulate_tty=True,
        parameters=[
            {
                "vid": ParameterValue(vid, value_type=str),
                "pid": ParameterValue(pid, value_type=str),
            }
        ],
    )

    ld = LaunchDescription()
    ld.add_action(declare_vid)
    ld.add_action(declare_pid)
    ld.add_action(serial_driver_node)

    return ld