from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    fcu_url_arg = DeclareLaunchArgument('fcu_url', default_value='udp://:14550@127.0.0.1:14555')
    gcs_url_arg = DeclareLaunchArgument('gcs_url', default_value='')
    tgt_system_arg = DeclareLaunchArgument('tgt_system', default_value='1')
    tgt_component_arg = DeclareLaunchArgument('tgt_component', default_value='1')
    log_output_arg = DeclareLaunchArgument('log_output', default_value='screen')
    respawn_mavros_arg = DeclareLaunchArgument('respawn_mavros', default_value='true')
    mavros_ns_arg = DeclareLaunchArgument('mavros_ns', default_value='/mavros')
    
    config_yaml_path = os.path.join(
        get_package_share_directory('iq_sim_ros2'),
        'launch', 'mavros_param.yaml'
    )
    config_yaml_arg = DeclareLaunchArgument('config_yaml', default_value=config_yaml_path)
    
    plugin_yaml_path = os.path.join(
        get_package_share_directory('mavros'),
        'launch', 'apm_pluginlists.yaml'
    )

    plugin_yaml_arg = DeclareLaunchArgument('plugin_yaml', default_value=plugin_yaml_path)

    # Include mavros_node launch
    mavros_launch = Node(
        package='mavros',
        executable='mavros_node',
        namespace=LaunchConfiguration('mavros_ns'),
        output=LaunchConfiguration('log_output'),
        respawn=LaunchConfiguration('respawn_mavros'),
        parameters=[
            config_yaml_path,
            plugin_yaml_path,
            {'fcu_url': LaunchConfiguration('fcu_url')},
            {'gcs_url': LaunchConfiguration('gcs_url')},
            {'target_system_id': LaunchConfiguration('tgt_system')},
            {'target_component_id': LaunchConfiguration('tgt_component')},
        ],
        arguments=['--ros-args', '--log-level', 'INFO']
    )
    
    return LaunchDescription([
        fcu_url_arg,
        gcs_url_arg,
        tgt_system_arg,
        tgt_component_arg,
        log_output_arg,
        respawn_mavros_arg,
        mavros_ns_arg,
        config_yaml_arg,
        plugin_yaml_arg,
        mavros_launch
    ])
