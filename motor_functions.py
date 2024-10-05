import RPio.GPIO as GPIO
import time

# L298N Driver 1 for front wheels

input1 = 17 # white wire
input2 = 22 # brown wire
input3 = 23 # organge wite
input4 = 24 # red wire
enableA1 = 12 # white wire (on oppsite side of GPIO PIN 17)
enableB1 = 13 # blue wire

# yellow wire is connected to GND on L298n

pwm_enA1 = None
pwm_enB1 = None

# L298 Driver 2 for back wheels

#input5 = 4
#input6 = 5
#input7 = 10
#input8 = 16
#enableA2 = 14
#enableB2 =  6

#pwm_enA2 = None
#pwm_enB2 = None

# Initializes all GPIO Pins

def init():

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
    enableA1 = 12 
    GPIO.setup(enableA1, GPIO.OUT)

    enableB1 = 13
    GPIO.setup(enableB2, GPIO.OUT) 


    pwm_left = GPIO.PWM(enableA1, 1000) # left side motor
    pwm_left.start(0)

    pwm_right = GPIO.PWM(enableB1, 1000) # right side motor
    pwm_right.start(0)
    
     # GPIO PIN 4
    #GPIO.setup(input5, GPIO.OUT)

    # GPIO PIN 5
    #GPIO.setup(input6, GPIO.OUT)

    # GPIO PIN 10
    #GPIO.setup(input7, GPIO.OUT)

    # GPIO PIN 16
    #GPIO.setup(input8, GPIO.OUT)

    # Controls speed and torque of motor
    #enableA2 = 14
    #GPIO.setup(enableA, GPIO.OUT)

    #enableB2 = 6
    #GPIO.setup(enableB2, GPIO.OUT) 
    
    #pwm_enA2 = GPIO.PWM(enableA2, 1000) 
    #pwm_enA2.start(0)

    #pwm_enB2 = GPIO.PWM(enableA2, 1000)
    #pwm_enB2.start(0)


def forward():
    
    # Forward motion because of H-Bridge component

    GPIO.output(input1, GPIO.HIGH)

    GPIO.output(input2, GPIO.LOW)

    GPIO.output(input3, GPIO.HIGH)

    GPIO.output(input4, GPIO.LOW)
    
    pwm_enA1.ChangeDutyCycle(75)

    pwm_enB1.ChangeDutyCycle(75)
    

def slow_forward():

    GPIO.output(input1, GPIO.HIGH)

    GPIO.output(input2, GPIO.LOW)

    GPIO.output(input3, GPIO.HIGH)

    GPIO.output(input4, GPIO.LOW)
    
    pwm_left.ChangeDutyCycle(25)

    pwm_right.ChangeDutyCycle(25)

def right_turn_15(): 

    # needs testing
    
    pwm_left.ChangeDutyCycle(35)
    pwm_right.ChangeDutyCycle(50)
    time.sleep(0.25)
    forward()


def right_turn_30():

    pwm_left.ChangeDutyCycle(35)
    pwm_right.ChangeDutyCycle(50)
    time.sleep(0.5)
    forward()

def right_turn_45():

    pwm_left.ChangeDutyCycle(35)
    pwm_right.ChangeDutyCycle(50)
    time.sleep(1)
    forward()

def left_turn_15():

    pwm_left.ChangeDutyCycle(50)
    pwm_right.ChangeDutyCycle(35)
    time.sleep(0.25)
    forward()

def left_turn_30():

    pwm_left.ChangeDutyCycle(50)
    pwm_right.ChangeDutyCycle(35)
    time.sleep(0.50)
    forward()

def left_turn_45():

    pwm_left.ChangeDutyCycle(50)
    pwm_right.ChangeDutyCycle(35)
    time.sleep(1)
    forward()

def stop():
    
    # Turns off all motors

    GPIO.output(input1, GPIO.LOW)

    GPIO.output(input2, GPIO.LOW)

    GPIO.output(input3, GPIO.LOW)

    GPIO.output(input4, GPIO.LOW)
    
    pwm_left.ChangeDutyCycle(0)

    pwm_right.ChangeDutyCycle(0)

def quit():

    GPIO.output(input1, GPIO.LOW)

    GPIO.output(input2, GPIO.LOW)

    GPIO.output(input3, GPIO.LOW)

    GPIO.output(input4, GPIO.LOW)

    pwm_left.ChangeDutyCycle(0)

    pwm_right.ChangeDutyCycle(0)

    pwm_left.stop()

    pwm_right.stop()

    GPIO.cleanup


# Optional if we have time:

# def speed_up()
# def reverse()
# def drift() if possible
