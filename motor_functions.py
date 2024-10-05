import RPio.GPIO as GPIO
import time


input1 = 17
input2 = 22
input3 = 23
input4 = 24
enableA = 12
enableB = 13


# Initializes all GPIO Pins

def init():

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
    enableA = 12 
    GPIO.setup(enableA, GPIO.OUT)

    enableB = 13
    GPIO.setup(enableB, GPIO.OUT) 
    
    pwm_enA = GPIO.PWM(enableA, 1000) 
    pwm_enA.start(0)

    pwm_enB = GPIO.PWM(enableA, 1000)
    pwm_enB.start(0)


def forward():
    
    # Forward motion because of H-Bridge component

    GPIO.output(input1, GPIO.HIGH)

    GPIO.output(input2, GPIO.LOW)

    GPIO.output(input3, GPIO.HIGH)

    GPIO.output(input4, GPIO.LOW)
    
    pwm_enA.ChangeDutyCycle(75)

    pwm_enB.ChangeDutyCycle(75)
    

#def slow_forward():
    



def stop():
    
    # Turns off all motors

    GPIO.output(input1, GPIO.LOW)

    GPIO.output(input2, GPIO.LOW)

    GPIO.output(input3, GPIO.LOW)

    GPIO.output(input4, GPIO.LOW)
    
    pwm_enA.ChangeDutyCycle(0)

    pwm_enB.ChangeDutyCycle(0)
