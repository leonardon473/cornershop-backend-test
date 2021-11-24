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
    class Meta:
        model = FoodDish
        fields = [
            'food',
        ]


class MenuOfTheDayUpdateSerializer(serializers.ModelSerializer):
    food_dishes = FoodDishSerializer(many=True)

    class Meta:
        model = MenuOfTheDay
        fields = [
            'date',
            'food_dishes',
        ]

    def create(self, validated_data: 'Dict[str, Any]'):

        food_dishes: 'List[Dict[str, Any]]' = validated_data.pop('food_dishes')

        instance: MenuOfTheDay = super().create(validated_data)

        for food_dish in food_dishes:
            FoodDish.objects.create(
                menu_of_the_day=instance,
                **food_dish,

            )

        return instance

    def to_representation(self, instance: MenuOfTheDay):
        return MenuOfTheDayRetrieveSerializer(instance).data


class MenuOfTheDayRetrieveSerializer(serializers.ModelSerializer):
    food_dishes = FoodDishSerializer(many=True)

    class Meta:
        model = MenuOfTheDay
        fields = [
            'id',
            'date',
            'food_dishes',
        ]


class MenuOfTheDayRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuOfTheDayUpdateSerializer

    def get_queryset(self):
        return MenuOfTheDay.objects.all()
