from datetime import datetime
from time import sleep
from light_controller import toggle_light
from notification_controller import send_notification
from models import Alarm, AlarmToggleEvent, db
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

r = SimpleMFRC522()

GPIO.setwarnings(False)


def read_card(reader: SimpleMFRC522):
    id, _ = reader.read()
    return str(id)


db.connect()


if __name__ == "__main__":
    while True:
        toggle_light("red")
        card_id = read_card()

        try:
            alarm = Alarm.get(admin_id=card_id)
        except Alarm.DoesNotExist:
            print(f"Alarm with admin ID {card_id} not found")
            send_notification(f"Unauthorized access attempt with admin ID {card_id}")
            sleep(10)
            continue
        alarm.is_active = not alarm.is_active
        alarm.save()
        print(f"{alarm.name} is now {'active' if alarm.is_active else 'inactive'}")
        send_notification(
            f"{alarm.name} is now {'active' if alarm.is_active else 'inactive'}"
        )
        if alarm.is_active:
            toggle_light("green")
        else:
            toggle_light("red")
        alarm_toggle_event = AlarmToggleEvent(
            alarm=alarm, timestamp=datetime.now(), toggled_to=alarm.is_active
        )
        alarm_toggle_event.save()
        print(f"Alarm toggle event saved: {alarm_toggle_event}")
        print("Waiting 10 seconds before next read")
        sleep(10)
