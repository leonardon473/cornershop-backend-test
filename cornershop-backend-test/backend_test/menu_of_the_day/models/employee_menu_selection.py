# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
import uuid
from typing import TYPE_CHECKING, cast

# Third party libs
from django.db import models

# Project libs


# App libs

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Optional

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
        "uuid.UUID",
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    )
    employee = cast(
        "Employee",
        models.ForeignKey(
            "menu_of_the_day.Employee",
            on_delete=models.PROTECT,  # type: ignore
        ),
    )

    selected_food_dish_id: "Optional[int]"
    selected_food_dish = cast(
        "FoodDish",
        models.ForeignKey(
            "menu_of_the_day.FoodDish",
            blank=True,
            null=True,
            on_delete=models.PROTECT,  # type: ignore
        ),
    )

    food_dish_customization = cast(
        str,
        models.CharField(
            blank=True,
            max_length=120,
        ),
    )

    menu_of_the_day = cast(
        "MenuOfTheDay",
        models.ForeignKey(
            "menu_of_the_day.MenuOfTheDay",
            on_delete=models.PROTECT,  # type: ignore
        ),
    )

    objects: "models.Manager[EmployeeMenuSelection]"

    class Meta:
        unique_together = (
            "employee",
            "menu_of_the_day",
        )
