# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateAPIView

# Project libs
from backend_test.menu_of_the_day.models import EmployeeMenuSelection
from backend_test.menu_of_the_day.services.update_employee_menu_selection import (
    TimeLimitToOrderReachedException,
    update_employee_menu_selection_service,
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
            "selected_food_dish",
            "food_dish_customization",
        ]

    def to_representation(self, instance: EmployeeMenuSelection) -> "Dict[str, Any]":
        return EmployeeMenuSelectionRetrieveSerializer(instance).data

    def update(
        self, instance: "EmployeeMenuSelection", validated_data: "Dict[str, Any]"
    ):
        try:
            return update_employee_menu_selection_service(
                employee_menu_selection=instance,
                selected_food_dish_id=validated_data["selected_food_dish"].id,
                food_dish_customization=validated_data["food_dish_customization"],
            )
        except TimeLimitToOrderReachedException:
            raise ValidationError(
                "El horario maximo para ordenar es a las 11:00",
                "time_limit_to_order_reached",
            )


# ---------------------
#  Retrieve Serializer
# ---------------------

#
# Serializer Deep level 2
#


class FoodDishSerializer(serializers.Serializer):
    id = serializers.IntegerField()
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
    food_dish_customization = serializers.CharField()
    selected_food_dish_id = serializers.IntegerField()
    menu_of_the_day = MenuOfTheDaySerializer()


# ------
#  View
# ------


class EmployeeMenuSelectionRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = EmployeeMenuSelectionUpdateSerializer

    def get_queryset(self):
        return EmployeeMenuSelection.objects.all()

    def patch(self, *args: "Any", **kwargs: "Any"):
        # Patch method is deleted to simplify logic
        raise MethodNotAllowed(method="patch")
