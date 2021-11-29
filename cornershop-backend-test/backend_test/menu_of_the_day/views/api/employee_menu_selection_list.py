# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

# Project libs
from backend_test.menu_of_the_day.models import EmployeeMenuSelection

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


# -------------
#  Serializers
# -------------


#
# Serializer Deep level 1
#


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()


class SelectedFoodDishSerializer(serializers.Serializer):
    food = serializers.CharField()


#
# Serializer Deep level main
#


class EmployeeMenuSelectionListSerializer(serializers.Serializer):
    id = serializers.CharField
    employee = EmployeeSerializer()
    food_dish_customization = serializers.CharField()
    selected_food_dish = SelectedFoodDishSerializer()


# ------
#  View
# ------


class EmployeeMenuSelectionListView(ListAPIView):
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminUser,)
    serializer_class = EmployeeMenuSelectionListSerializer

    def get_queryset(self):
        menu_date = self.request.query_params.get("menu_date")
        if not menu_date:
            EmployeeMenuSelection.objects.none()

        return EmployeeMenuSelection.objects.filter(
            menu_of_the_day__date=menu_date, selected_food_dish__isnull=False
        )
