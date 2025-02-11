from models import Alarm
from time import sleep
import RPi.GPIO as GPIO
from light_controller import toggle_light
from notification_controller import send_notification


PIR_PIN = 23  # Adjust if using a different GPIO pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
sleep(2)


def motion_detector():
    return GPIO.input(PIR_PIN) == 1


def observe_movement():
    while True:
        sleep(1)
        alarms = list(Alarm.select().dicts().execute())
        is_alarm_active = any(alarm["is_active"] for alarm in alarms)

        if is_alarm_active:
            if motion_detector():
                toggle_light("red")
                print("intruder detected")
                send_notification("intruder detected")
            else:
                toggle_light("green")


observe_movement()
