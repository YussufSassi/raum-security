from typing import Union
from fastapi import FastAPI
from models import Alarm, AlarmToggleEvent, IntruderDetectionEvent
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AlarmDto(BaseModel):
    name: str
    admin_id: str


@app.get("/alarms")
def read_alarms():
    return list(Alarm.select().dicts())


@app.get("/events/{alarm_id}")
def read_events(alarm_id: int):
    events = (
        AlarmToggleEvent.select().where(AlarmToggleEvent.alarm_id == alarm_id).dicts()
    )
    intruder_detection_events = (
        IntruderDetectionEvent.select()
        .where(IntruderDetectionEvent.alarm_id == alarm_id)
        .dicts()
    )
    return list(events) + list(intruder_detection_events)


@app.delete("/alarms/{alarm_id}")
def delete_alarm(alarm_id: int):
    Alarm.delete().where(Alarm.id == alarm_id).execute()
    return {"success": True}


@app.post("/create-alarm")
def create_alarm(alarm: AlarmDto):
    print(alarm)
    try:
        db_alarm = Alarm(name=alarm.name, admin_id=alarm.admin_id)
        db_alarm.save()

    except Exception as e:
        return {"success": False, "error": str(e)}
    return {
        "id": db_alarm.id,
        "name": db_alarm.name,
        "admin_id": db_alarm.admin_id,
        "success": True,
    }
