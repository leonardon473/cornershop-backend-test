# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
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
    from typing import Any
    from datetime import date

    from celery.app import Celery

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


@app.on_after_configure.connect
def setup_periodic_tasks(sender: "Celery", **kwargs: "Any"):
    # Executes every day at 7:00 a.m.
    # Check the time zone conf of django.
    sender.add_periodic_task(
        crontab(
            hour=7,
            minute=0,
        ),
        send_menu_of_the_day_for_today_to_employees_task.s(),
    )
