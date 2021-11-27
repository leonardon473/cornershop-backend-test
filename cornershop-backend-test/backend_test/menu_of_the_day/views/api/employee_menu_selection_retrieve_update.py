# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateAPIView

# Project libs
from backend_test.menu_of_the_day.models import (
    EmployeeMenuSelection,
    FoodDish,
    MenuOfTheDay,
)

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Dict

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------

# -------------------
#  Update Serializer
# -------------------


class EmployeeMenuSelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:  # type: ignore
        model = EmployeeMenuSelection
        fields = [
            "food_dish",
        ]

    def to_representation(self, instance: EmployeeMenuSelection) -> "Dict[str, Any]":
        return EmployeeMenuSelectionRetrieveSerializer(instance).data


# ---------------------
#  Retrieve Serializer
# ---------------------

#
# Serializer Deep level 2
#


class FoodDishSerializer(serializers.Serializer):
    food = serializers.CharField()


#
# Serializer Deep level 1
#


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()


class MenuOfTheDaySerializer(serializers.Serializer):
    date = serializers.DateField()
    food_dishes = FoodDishSerializer(many=True)


#
# Serializer Deep level main
#


class EmployeeMenuSelectionRetrieveSerializer(serializers.Serializer):
    id = serializers.CharField
    employee = EmployeeSerializer()
    menu_of_the_day = MenuOfTheDaySerializer()


# ------
#  View
# ------


class EmployeeMenuSelectionRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = EmployeeMenuSelectionUpdateSerializer

    def get_queryset(self):
        return EmployeeMenuSelection.objects.all()
