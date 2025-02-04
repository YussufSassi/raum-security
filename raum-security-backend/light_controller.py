from constants import PRESENTATION_MODE

if PRESENTATION_MODE:
    from rpi_emulator import rpi_emulator
else:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    R = 13
    Y = 6
    G = 5

    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(Y, GPIO.OUT)
    GPIO.setup(G, GPIO.OUT)


def toggle_light(color: str):
    if PRESENTATION_MODE == False:
        if color == "red":
            GPIO.output(R, True)
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
    else:
        rpi_emulator.toggle_light(color)
