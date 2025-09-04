from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    mavros_share_dir = FindPackageShare('mavros')

    return LaunchDescription([
        Node(
            package="mavros",
            executable="mavros_node",
            name="mavros",
            namespace='drone1',
            output="screen",
            emulate_tty=True,
            parameters=[
                {'fcu_url': 'udp://127.0.0.1:14551@14555'},
                {'gcs_url': ''},
                {'target_system_id': 1},
                {'target_component_id': 1},
                {'fcu_protocol': 'v2.0'},
                PathJoinSubstitution([mavros_share_dir, 'launch', 'apm_pluginlists.yaml']),
                PathJoinSubstitution([mavros_share_dir, 'launch', 'apm_config.yaml']),
            ]
        ),
        Node(
            package="mavros",
            executable="mavros_node",
            name="mavros",
            namespace='drone2',
            output="screen",
            emulate_tty=True,
            parameters=[
                {'fcu_url': "udp://127.0.0.1:14561@14565"},
                {'gcs_url': ''},
                {'target_system_id': 2},
                {'target_component_id': 1},
                {'fcu_protocol': 'v2.0'},
                PathJoinSubstitution([mavros_share_dir, 'launch', 'apm_pluginlists.yaml']),
                PathJoinSubstitution([mavros_share_dir, 'launch', 'apm_config.yaml']),
            ]
        ),
        Node(
            package="mavros",
            executable="mavros_node",
            name="mavros",
            namespace='drone3',
            output="screen",
            emulate_tty=True,
            parameters=[
                {'fcu_url': "udp://127.0.0.1:14571@14575"},
                {'gcs_url': ''},
                {'target_system_id': 3},
                {'target_component_id': 1},
                {'fcu_protocol': 'v2.0'},
                PathJoinSubstitution([mavros_share_dir, 'launch', 'apm_pluginlists.yaml']),
                PathJoinSubstitution([mavros_share_dir, 'launch', 'apm_config.yaml']),
            ]
        ),
    ])
