from datetime import datetime

from django.conf import settings

from backend_test.menu_of_the_day.models import EmployeeMenuSelection
from backend_test.utils.time import localize, now


class TimeLimitToOrderReachedException(Exception):
    pass


def update_employee_menu_selection_service(
    employee_menu_selection: "EmployeeMenuSelection",
    selected_food_dish_id: int,
    food_dish_customization: str,
):
    """
    Update a instance of EmployeeMenuSelection.
    If the limit to order is exceeded a TimeLimitToOrderReachedException is
    raised.
    """
    menu_date = employee_menu_selection.menu_of_the_day.date
    menu_limit_to_order = localize(
        datetime.combine(menu_date, settings.TIME_LIMIT_TO_ORDER)
    )

    if now() < menu_limit_to_order:
        employee_menu_selection.selected_food_dish_id = selected_food_dish_id
        employee_menu_selection.food_dish_customization = food_dish_customization
        employee_menu_selection.save()
        return employee_menu_selection

    raise TimeLimitToOrderReachedException
