from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
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
        get_package_share_directory('iq_sim'),
        'launch', 'mavros_param.yaml'
    )
    config_yaml_arg = DeclareLaunchArgument('config_yaml', default_value=config_yaml_path)
    
    plugin_yaml_path = os.path.join(
        get_package_share_directory('mavros'),
        'launch', 'apm_pluginlists.yaml'
    )

    plugin_yaml_arg = DeclareLaunchArgument('plugin_yaml', default_value=plugin_yaml_path)

    mavros_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('iq_sim'), "launch", "mavros_node.launch.py")
        ),
        launch_arguments={
            'pluginlists_yaml': plugin_yaml_path,
            'config_yaml': config_yaml_path,
            'fcu_url': LaunchConfiguration('fcu_url'),
            'gcs_url': LaunchConfiguration('gcs_url'),
            'mavros_ns': LaunchConfiguration('mavros_ns'),
            'tgt_system': LaunchConfiguration('tgt_system'),
            'tgt_component': LaunchConfiguration('tgt_component'),
            'log_output': LaunchConfiguration('log_output'),
            'respawn_mavros': LaunchConfiguration('respawn_mavros'),
        }.items()
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
