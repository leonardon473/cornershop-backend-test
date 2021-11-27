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
    import datetime

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class MenuOfTheDay(models.Model):
    id: int

    date = cast("datetime.date", models.DateField(unique=True))
