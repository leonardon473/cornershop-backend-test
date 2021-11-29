# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.conf import settings
from celery.schedules import crontab

# Project libs
from backend_test.celery import app
from backend_test.menu_of_the_day.services.send_menu_of_the_day_to_employees import (
    send_menu_of_the_day_to_employees,
)
from backend_test.menu_of_the_day.services.update_employees import (
    update_emplooyes_from_slack,
)
from backend_test.utils.time import now

# If type checking, __all__
if TYPE_CHECKING:
    pass

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


@app.task
def send_menu_of_the_day_for_today_to_employees_task():
    menu_date = now().date()
    update_emplooyes_from_slack()
    try:
        send_menu_of_the_day_to_employees(menu_date)
        return True
    except ValueError:
        pass
    return False


# Executes every day at 7:00 a.m.
# Check the time zone conf of django and celery.
app.conf.beat_schedule["send_menu_of_the_day_for_today_to_employees_task"] = {
    "task": "backend_test.menu_of_the_day.tasks.send_menu_of_the_day_to_employees.send_menu_of_the_day_for_today_to_employees_task",
    "schedule": crontab(
        hour=settings.TIME_TO_SEND_MENU.hour,
        minute=settings.TIME_TO_SEND_MENU.minute,
    ),
    "args": (),
}
