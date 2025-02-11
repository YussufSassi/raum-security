from constants import MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT
from peewee import *

db = MySQLDatabase(
    MYSQL_DATABASE,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=int(MYSQL_PORT),
)


class Alarm(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    is_active = BooleanField(default=False)
    admin_id = CharField(max_length=255)

    class Meta:
        database = db
        table_name = "alarm"


class AlarmToggleEvent(Model):
    id = IntegerField(primary_key=True)
    alarm = ForeignKeyField(Alarm, backref="toggle_events")
    timestamp = DateTimeField()
    toggled_to = BooleanField()

    class Meta:
        database = db
        table_name = "alarm_toggle_event"


class IntruderDetectionEvent(Model):
    id = IntegerField(primary_key=True)
    timestamp = DateTimeField()
    alarm = ForeignKeyField(Alarm, backref="intruder_detection_events")

    class Meta:
        database = db
        table_name = "intruder_detection_event"


class ScheduleAlarmToggle(Model):
    id = IntegerField(primary_key=True)
    toggle_alarm_at = IntegerField()
    toggle_alarm_to = BooleanField()
    alarm = ForeignKeyField(Alarm, backref="schedule_alarm_toggles")

    class Meta:
        database = db
        table_name = "schedule_alarm_toggle"
