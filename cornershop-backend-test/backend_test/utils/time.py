# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from datetime import datetime
from typing import TYPE_CHECKING

# Third party libs
from django.utils import timezone

# Project libs

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


def now() -> datetime:
    return datetime.now(timezone.get_default_timezone())


def localize(dt: datetime) -> datetime:
    """
    Set default timezone to a datetime naive.
    """
    tz = timezone.get_default_timezone()
    return tz.localize(dt)
