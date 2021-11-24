# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING, cast

# Third party libs
from django.db import models

# Project libs


# App libs

# If type checking, __all__
if TYPE_CHECKING:
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


class FoodDish(models.Model):
    menu_of_the_day = cast(
        'MenuOfTheDay',
        models.ForeignKey(
            'menu_of_the_day.MenuOfTheDay',
            on_delete=models.PROTECT,  # type: ignore
        )
    )

    food = cast(
        str,
        models.CharField(max_length=140)
    )
