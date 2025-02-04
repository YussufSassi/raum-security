from dotenv import load_dotenv
import os

load_dotenv()


MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
NTFY_TOPIC = os.getenv("NTFY_TOPIC")
PRESENTATION_MODE = bool(os.getenv("PRESENTATION_MODE"))
