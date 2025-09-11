from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('fcu_url'),
        DeclareLaunchArgument('gcs_url'),
        DeclareLaunchArgument('mavros_ns', default_value="/mavros"),
        DeclareLaunchArgument('tgt_system'),
        DeclareLaunchArgument('tgt_component'),
        DeclareLaunchArgument('pluginlists_yaml'),
        DeclareLaunchArgument('config_yaml'),
        DeclareLaunchArgument('log_output', default_value="screen"),
        DeclareLaunchArgument('fcu_protocol', default_value="v2.0"),
        DeclareLaunchArgument('respawn_mavros', default_value="true"),

        Node(
            package="mavros",
            executable="mavros_node",
            namespace=LaunchConfiguration('mavros_ns'),
            output=LaunchConfiguration('log_output'),
            respawn=LaunchConfiguration('respawn_mavros'),
            parameters=[
                {'pluginlists_yaml': LaunchConfiguration('pluginlists_yaml')},
                {'config_yaml' : LaunchConfiguration('config_yaml')},
                {'fcu_url': LaunchConfiguration('fcu_url')},
                {'gcs_url': LaunchConfiguration('gcs_url')},
                {'tgt_system': LaunchConfiguration('tgt_system')},
                {'tgt_component': LaunchConfiguration('tgt_component')},
                {'fcu_protocol': LaunchConfiguration('fcu_protocol')},
                {'respawn_mavros': LaunchConfiguration('respawn_mavros')},
            ],
            arguments=['--ros-args', '--log-level', 'INFO']
        )
    ])
