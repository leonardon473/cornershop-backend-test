# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import serializers

# Project libs
from backend_test.menu_of_the_day.models import FoodDish, MenuOfTheDay
from backend_test.utils.rest_framework.serializers import UpdatableListModelSerializer

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Dict, List

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class FoodDishSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:  # type: ignore
        list_serializer_class = UpdatableListModelSerializer
        model = FoodDish
        fields = [
            "id",
            "food",
        ]


class MenuOfTheDayUpdateSerializer(serializers.ModelSerializer):
    food_dishes = FoodDishSerializer(many=True)

    class Meta:  # type: ignore
        model = MenuOfTheDay
        fields = [
            "date",
            "food_dishes",
        ]

    def update(self, instance: "MenuOfTheDay", validated_data: "Dict[str, Any]"):

        food_dishes: "List[Dict[str, Any]]" = validated_data.pop("food_dishes")

        instance = super().update(instance, validated_data)  # type: ignore

        self.fields["food_dishes"].update(  # type: ignore
            instance=instance, validated_data=food_dishes
        )

        return instance

    def to_representation(self, instance: MenuOfTheDay) -> "Dict[str, Any]":
        return MenuOfTheDayRetrieveSerializer(instance).data


class MenuOfTheDayRetrieveSerializer(serializers.ModelSerializer):
    food_dishes = FoodDishSerializer(many=True)

    class Meta:
        model = MenuOfTheDay
        fields = [
            "id",
            "date",
            "food_dishes",
        ]


class MenuOfTheDayRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuOfTheDayUpdateSerializer

    def get_queryset(self):
        return MenuOfTheDay.objects.all()
