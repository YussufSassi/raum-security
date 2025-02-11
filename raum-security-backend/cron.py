from models import ScheduleAlarmToggle, Alarm
from datetime import datetime
from time import sleep


def scheduled_alarm_toggles():
    schedule_alarm_toggles = list(ScheduleAlarmToggle.select().dicts().execute())
    for schedule_alarm_toggle in schedule_alarm_toggles:
        if schedule_alarm_toggle["toggle_alarm_at"] == datetime.now().hour:
            alarm = Alarm.get_by_id(schedule_alarm_toggle["alarm_id"])
            alarm.is_active = schedule_alarm_toggle["toggle_alarm_to"]
            alarm.save()


while True:
    scheduled_alarm_toggles()
    sleep(3600)
