import requests as r
from constants import NTFY_TOPIC


def send_notification(message: str):
    NTFY_URL = f"https://ntfy.sh/{NTFY_TOPIC}"
    r.post(NTFY_URL, data=message)
