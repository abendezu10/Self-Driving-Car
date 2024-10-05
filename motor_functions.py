import RPio.GPIO as GPIO
import time


# Initializes all GPIO Pins

def init():

    GPIO.setmode(GPIO.BCM)

    # GPIO PIN 17
    input1 = 17
    GPIO.setup(input1, GPIO.OUT)

    # GPIO PIN 22
    input2 = 22
    GPIO.setup(input2, GPIO.OUT)

    # GPIO PIN 23
    input3 = 23
    GPIO.setup(input3, GPIO.OUT)

    # GPIO PIN 24
    input4 = 24
    GPIO.setup(input4, GPIO.OUT)

    # Controls speed and torque of motor
    enableA = 12 
    GPIO.setup(enableA, GPIO.OUT)

    enableB = 13
    GPIO.setup(enableB, GPIO.OUT)

    
    GPIO.output(enableA, GPIO.HIGH)
    GPIO.output(enableB, GPIO.LOW)

