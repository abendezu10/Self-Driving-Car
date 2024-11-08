import RPi.GPIO as GPIO
import time

# L298N Driver 1 for front wheels

input1 = 17 # white wire
input2 = 22 # brown wire
input3 = 23 # organge wite
input4 = 24 # red wire
enableA1 = 12 # white wire (on oppsite side of GPIO PIN 17)
enableB1 = 13 # blue wire

# yellow wire is connected to GND on L298n

# L298 Driver 2 for back wheels

#input5 = 4
#input6 = 5
#input7 = 10
#input8 = 16
#enableA2 = 14
#enableB2 = 6

#pwm_enA2 = None
#pwm_enB2 = None

# Initializes all GPIO Pins

class MotorController:

    def __init__(self):
        
        global pwm_left,pwm_right

        GPIO.setmode(GPIO.BCM)

        # GPIO PIN 17
        GPIO.setup(input1, GPIO.OUT)

        # GPIO PIN 22
        GPIO.setup(input2, GPIO.OUT)

        # GPIO PIN 23
        GPIO.setup(input3, GPIO.OUT)

        # GPIO PIN 24
        GPIO.setup(input4, GPIO.OUT)

        # Controls speed and torque of motor
        GPIO.setup(enableA1, GPIO.OUT)

        GPIO.setup(enableB1, GPIO.OUT) 


        self.pwm_left = GPIO.PWM(enableA1, 1000) # left side motor
        self.pwm_left.start(0)

        self.pwm_right = GPIO.PWM(enableB1, 1000) # right side motor
        self.pwm_right.start(0)
    
    def forward(self):
    
        # Forward motion because of H-Bridge component

        GPIO.output(input1, GPIO.HIGH)

        GPIO.output(input2, GPIO.LOW)

        GPIO.output(input3, GPIO.HIGH)

        GPIO.output(input4, GPIO.LOW)

        self.pwm_left.ChangeDutyCycle(100)

        self.pwm_right.ChangeDutyCycle(100)
    

    def slow_forward(self):

        GPIO.output(input1, GPIO.HIGH)

        GPIO.output(input2, GPIO.LOW)

        GPIO.output(input3, GPIO.HIGH)

        GPIO.output(input4, GPIO.LOW)
    
        self.pwm_left.ChangeDutyCycle(50)

        self.pwm_right.ChangeDutyCycle(50)

    def right_turn_15(self): 

        # needs testing
    
        self.pwm_left.ChangeDutyCycle(35)
        self.pwm_right.ChangeDutyCycle(50)
        time.sleep(0.25)
        self.forward()


    def right_turn_30(self):

        self.pwm_left.ChangeDutyCycle(35)
        self.pwm_right.ChangeDutyCycle(50)
        time.sleep(0.5)
        self.forward()

    def right_turn_45(self):

        self.pwm_left.ChangeDutyCycle(35)
        self.pwm_right.ChangeDutyCycle(50)
        time.sleep(1)
        self.forward()

    def left_turn_15(self):

        self.pwm_left.ChangeDutyCycle(50)
        self.pwm_right.ChangeDutyCycle(35)
        time.sleep(0.25)
        self.forward()

    def left_turn_30(self):

        self.pwm_left.ChangeDutyCycle(50)
        self.pwm_right.ChangeDutyCycle(35)
        time.sleep(0.50)
        self.forward()

    def left_turn_45(self):

        self.pwm_left.ChangeDutyCycle(50)
        self.pwm_right.ChangeDutyCycle(35)
        time.sleep(1)
        self.forward()

    def stop(self):
    
        # Turns off all motors

        GPIO.output(input1, GPIO.LOW)

        GPIO.output(input2, GPIO.LOW)

        GPIO.output(input3, GPIO.LOW)

        GPIO.output(input4, GPIO.LOW)
    
        self.pwm_left.ChangeDutyCycle(0)

        self.pwm_right.ChangeDutyCycle(0)

    def quit(self):

        GPIO.output(input1, GPIO.LOW)

        GPIO.output(input2, GPIO.LOW)

        GPIO.output(input3, GPIO.LOW)

        GPIO.output(input4, GPIO.LOW)

        self.pwm_left.ChangeDutyCycle(0)

        self.pwm_right.ChangeDutyCycle(0)

        self.pwm_left.stop()

        self.pwm_right.stop()

        GPIO.cleanup()


# Optional if we have time:

# def speed_up()
# def reverse()
# def drift() if possible
