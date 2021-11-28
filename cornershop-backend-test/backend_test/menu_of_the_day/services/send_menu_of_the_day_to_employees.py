from datetime import date

from django.conf import settings

from backend_test.menu_of_the_day.integrations.slack import (
    send_message_to_slack_user,
)
from backend_test.menu_of_the_day.models import (
    Employee,
    EmployeeMenuSelection,
    MenuOfTheDay,
)


def send_menu_of_the_day_to_employees(menu_date: "date"):
    """
    menu_date: Date of the MenuOfTheDate
    """
    menu_of_the_day = MenuOfTheDay.objects.get(date=menu_date)
    for employee in Employee.objects.all():
        employee_menu_selection = EmployeeMenuSelection.objects.create(
            employee_id=employee.id, menu_of_the_day=menu_of_the_day
        )
        link = f"{settings.BACKEND_HOST}menu/{employee_menu_selection.id}"
        message = (
            f"Hola {employee.name} \n"
            f"En este link {link} puedes "
            "seleccionar lo que quieras comer el día "
            f"{menu_of_the_day.date.strftime('%d/%m/%Y')}. \n"
            "Esperamos lo disfrutes."
        )
        send_message_to_slack_user(message, employee.slack_id)
