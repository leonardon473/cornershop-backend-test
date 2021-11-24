# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING, cast
import uuid

# Third party libs
from django.db import models

# Project libs


# App libs

# If type checking, __all__
if TYPE_CHECKING:
    from backend_test.menu_of_the_day.models.employee import Employee
    from backend_test.menu_of_the_day.models.food_dish import FoodDish
    from backend_test.menu_of_the_day.models.menu_of_the_day import MenuOfTheDay

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class EmployeeMenuSelection(models.Model):
    id = cast(
        'uuid.UUID',
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    )
    employee = cast(
        'Employee',
        models.ForeignKey(
            'menu_of_the_day.Employee',
            on_delete=models.PROTECT,  # type: ignore
        )
    )

    food_dish = cast(
        'FoodDish',
        models.ForeignKey(
            'menu_of_the_day.FoodDish',
            on_delete=models.PROTECT,  # type: ignore
        )
    )

    menu_of_the_day = cast(
        'MenuOfTheDay',
        models.ForeignKey(
            'menu_of_the_day.MenuOfTheDay',
            on_delete=models.PROTECT,  # type: ignore
        )
    )
