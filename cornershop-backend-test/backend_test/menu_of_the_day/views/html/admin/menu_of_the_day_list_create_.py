# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# Project libs

# If type checking, __all__
if TYPE_CHECKING:
    from django.http import HttpRequest

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


@staff_member_required
def menu_of_the_day_list_create(request: "HttpRequest"):
    # View code here...
    return render(request, "menu_of_the_day_list_create.html")


# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------
