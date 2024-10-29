from datetime import datetime
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
from peewee import *
from dotenv import load_dotenv
import os

load_dotenv()

db = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host="127.0.0.1",
    port=3306,
)


class Alarm(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    is_active = BooleanField(default=False)
    admin_id = CharField(max_length=255)

    class Meta:
        database = db


class AlarmToggleEvent(Model):
    id = IntegerField(primary_key=True)
    alarm = ForeignKeyField(Alarm, backref="toggle_events")
    timestamp = DateTimeField()

    class Meta:
        database = db
        table_name = "alarm_toggle_event"


r = SimpleMFRC522()

db.connect()


def read_card(reader: SimpleMFRC522):
    id = reader.read()
    return id


if __name__ == "__main__":
    while True:
        card_id = read_card(r)
        alarm = Alarm.get(admin_id=card_id)
        if not alarm:
            print(f"Alarm with admin ID {card_id} not found")
            continue
        alarm.is_active = not alarm.is_active
        alarm.save()
        print(
            f"Alarm {alarm.name} is now {'active' if alarm.is_active else 'inactive'}"
        )
        alarm_toggle_event = AlarmToggleEvent(alarm=alarm, timestamp=datetime.now())
        alarm_toggle_event.save()
        print(f"Alarm toggle event saved: {alarm_toggle_event}")
