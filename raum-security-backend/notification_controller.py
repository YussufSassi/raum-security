import requests as r
from dotenv import load_dotenv
import os

load_dotenv()


def send_notification(message: str):
    NTFY_URL = f"https://ntfy.sh/{os.getenv('NTFY_TOPIC')}"
    r.post(NTFY_URL, data=message)
