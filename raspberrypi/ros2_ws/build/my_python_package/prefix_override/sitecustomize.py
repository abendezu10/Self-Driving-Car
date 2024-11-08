import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abendezu/Documents/Projects/Self-Driving-Car/raspberrypi/ros2_ws/install/my_python_package'
