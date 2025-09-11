from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, EnvironmentVariable
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    return LaunchDescription([
        SetEnvironmentVariable(
            'GAZEBO_MODEL_PATH',
            [
                PathJoinSubstitution([FindPackageShare('iq_sim'), 'models']),
                ':',
                EnvironmentVariable('GAZEBO_MODEL_PATH', default_value=''),
                ':',
                os.path.expanduser('~/ardupilot_gazebo/models')
            ]
        ),
        
        SetEnvironmentVariable(
            'GAZEBO_PLUGIN_PATH',
            [
                EnvironmentVariable('GAZEBO_PLUGIN_PATH', default_value=''),
                ':',
                os.path.expanduser('~/ardupilot_gazebo/build')
            ]
        ),
        
        SetEnvironmentVariable('GAZEBO_MODEL_DATABASE_URI', ''),
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('gazebo_ros'),
                    'launch',
                    'gazebo.launch.py'    
                ])
            ),
            launch_arguments=[
                ('world', PathJoinSubstitution([FindPackageShare('iq_sim'), 'worlds', 'vtol.world']))
            ]
        )
    ])
