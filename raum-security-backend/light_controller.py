from typing import Literal
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

R = 17  # Red
Y = 27  # Yellow
G = 22  # Green

GPIO.setup(R, GPIO.OUT)
GPIO.setup(Y, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)


def toggle_light(color: Literal["red", "yellow", "green"]):
    if color == "red":
        GPIO.output(R, GPIO.HIGH)
        GPIO.output(Y, False)
        GPIO.output(G, False)
    elif color == "yellow":
        GPIO.output(R, False)
        GPIO.output(Y, True)
        GPIO.output(G, False)
    elif color == "green":
        GPIO.output(R, False)
        GPIO.output(Y, False)
        GPIO.output(G, True)
