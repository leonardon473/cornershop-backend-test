# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.shortcuts import render

# Project libs

# App libs

# If type checking, __all__
if TYPE_CHECKING:
    from django.http import HttpRequest

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def menu_of_the_day_retrieve_update_destroy(request: 'HttpRequest', id: int):
    # View code here...
    return render(request, 'menu_of_the_day_retrieve_update_destroy.html')

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------
