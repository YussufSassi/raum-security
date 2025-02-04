const API_URL = "http://0.0.0.0:8502"

export type Alarm = {
  id?: number
  name: string
  admin_id: string
  is_active?: boolean
}

export type AlarmActivationToggleEvent = {
    id: number
    alarm: number
    timestamp: string
    toggled_to: boolean
}


export const api = {
  getAlarms: () => fetch(`${API_URL}/alarms`).then((res) => res.json() as Promise<Alarm[]>),
  getEventsByAlarmId: (alarmId: string) =>
    fetch(`${API_URL}/events/${alarmId}`).then((res) => res.json() as Promise<AlarmActivationToggleEvent[]>),
  createAlarm: (alarm: Alarm) =>
    fetch(`${API_URL}/create-alarm`, {
      method: "POST",
      headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(alarm),
    }).then((res) => res.json()),
  deleteAlarm: (alarmId: number) =>
    fetch(`${API_URL}/alarms/${alarmId}`, {
      method: "DELETE",
    }).then((res) => res.json()),
};
