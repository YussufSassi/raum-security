from rpi_emulator import rpi_emulator
from constants import PRESENTATION_MODE
from models import Alarm
from time import sleep


def observe_movement():
    if PRESENTATION_MODE:
        alarms = list(Alarm.select().dicts().execute())

        for alarm in alarms:
            if alarm["is_active"]:
                return rpi_emulator.observe_movement(True)
            return rpi_emulator.observe_movement(False)

    else:
        movement = rpi_emulator.observe_movement(True)

    return movement


def detect_intruders():
    while True:
        sleep(1)
        movement = observe_movement()
        if movement:
            print("detected intruder")
            rpi_emulator.ring_alarm(True)


print(detect_intruders())
