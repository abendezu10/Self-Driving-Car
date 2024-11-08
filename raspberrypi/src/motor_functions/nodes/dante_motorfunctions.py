import rlcpy
from rlcpy import Node
from std_msgs.msg import String
import motor_functions 


class Subscriber(Node):
       
    def __init__(self):
        super().__init__('motor_functions')
        self.motor_functions_ = MotorController()
        self.motor_subscription = self.create_subscription(
            String, 
            'motor_commands', 
            self.directioncallback, 
            10)

        self.motor_functions_
        self.motor_subsciption

    def direction_callback(self, msg):
        dir_command = msg.data.lower()
        
        if(dir_command == 'forward'):
            self.get_logger().info('moving forward...')
            self.motor_functions_.forward()
        else if(dir_command == 'stop'):
            self.get_logger().info('stopping...')
            self.motor_functions_.stop()
        
            

        




def main(args==None):
    p

if __name__ == '__main__':
    main()
