from ..envtools import getenv, parse_time

BACKEND_HOST = getenv("BACKEND_HOST")
if not BACKEND_HOST.endswith("/"):
    BACKEND_HOST = BACKEND_HOST + "/"

# Used to limit the time employees can order their menu. Format "HH:MM".
TIME_LIMIT_TO_ORDER = getenv("TIME_LIMIT_TO_ORDER", coalesce=parse_time)

# Time when the menu of the day is sent to employees. Format "HH:MM".
TIME_TO_SEND_MENU = getenv("TIME_TO_SEND_MENU", coalesce=parse_time)
