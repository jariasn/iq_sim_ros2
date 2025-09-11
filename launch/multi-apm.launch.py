from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config_yaml_path = os.path.join(
        get_package_share_directory('iq_sim'),
        'launch', 'mavros_param.yaml'
    )
    
    plugin_yaml_path = os.path.join(
        get_package_share_directory('mavros'),
        'launch', 'apm_pluginlists.yaml'
    )

    return LaunchDescription([
        Node(
            package="mavros",
            executable="mavros_node",
            name="mavros",
            namespace='/drone1',
            output="screen",
            emulate_tty=True,
            parameters=[
                {'pluginlists_yaml': plugin_yaml_path},
                {'config_yaml': config_yaml_path},
                {'fcu_url': 'udp://:14551@127.0.0.1:14555'},
                {'gcs_url': ''},
                {'target_system_id': 1},
                {'target_component_id': 1},
                {'fcu_protocol': 'v2.0'},
            ]
        ),
        Node(
            package="mavros",
            executable="mavros_node",
            name="mavros",
            namespace='/drone2',
            output="screen",
            emulate_tty=True,
            parameters=[
                {'pluginlists_yaml': plugin_yaml_path},
                {'config_yaml': config_yaml_path},
                {'fcu_url': "udp://:14561@127.0.0.1:14565"},
                {'gcs_url': ''},
                {'target_system_id': 2},
                {'target_component_id': 1},
                {'fcu_protocol': 'v2.0'},
            ]
        ),
        Node(
            package="mavros",
            executable="mavros_node",
            name="mavros",
            namespace='/drone3',
            output="screen",
            emulate_tty=True,
            parameters=[
                {'pluginlists_yaml': plugin_yaml_path},
                {'config_yaml': config_yaml_path},
                {'fcu_url': "udp://:14571@127.0.0.1:14575"},
                {'gcs_url': ''},
                {'target_system_id': 3},
                {'target_component_id': 1},
                {'fcu_protocol': 'v2.0'},
            ]
        ),
    ])
