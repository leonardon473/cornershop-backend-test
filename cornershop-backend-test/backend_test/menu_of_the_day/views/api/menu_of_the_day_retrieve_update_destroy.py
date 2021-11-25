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


class FoodDishListSerializer(serializers.ListSerializer):
    """
    Class created due to update method is not defined by default due to
    is unclear how to deal with insertions and deletions.
    """

    def update(self,
               instance: MenuOfTheDay,
               validated_data: 'List[Dict[str, Any]]'
               ) -> 'List[FoodDish]':

        serializer = FoodDishSerializer()
        # Delete objects not present in validated data
        FoodDish.objects.exclude(
            id__in=[i['id'] for i in validated_data if i.get('id')],
            menu_of_the_day=instance
        ).delete()
        food_dishes: 'List[FoodDish]' = []
        for food_dish_data in validated_data:
            if food_dish_data.get('id'):
                food_dish = FoodDish.objects.get(
                    id=food_dish_data['id'],
                    menu_of_the_day=instance
                )
                serializer.update(  # type: ignore
                    instance=food_dish,
                    validated_data=food_dish_data
                )
                food_dishes.append(food_dish)
            else:
                food_dish_data['menu_of_the_day'] = instance
                serializer.create(  # type: ignore
                    validated_data=food_dish_data
                )

        return food_dishes


class FoodDishSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        list_serializer_class = FoodDishListSerializer
        model = FoodDish
        fields = [
            'id',
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

    def update(self, instance: 'MenuOfTheDay', validated_data: 'Dict[str, Any]'):

        food_dishes: 'List[Dict[str, Any]]' = validated_data.pop('food_dishes')

        instance = super().update(instance, validated_data)  # type: ignore

        self.fields['food_dishes'].update(  # type: ignore
            instance=instance,
            validated_data=food_dishes
        )

        return instance

    def to_representation(self, instance: MenuOfTheDay) -> 'Dict[str, Any]':
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
