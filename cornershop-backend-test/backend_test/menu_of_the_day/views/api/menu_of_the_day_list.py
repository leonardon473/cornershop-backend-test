from rest_framework.generics import ListAPIView
from rest_framework import serializers

from backend_test.menu_of_the_day.models import MenuOfTheDay


class MenuOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOfTheDay
        fields = [
            'id',
            'date',
        ]


class MenuOfTheDayListApiView(ListAPIView):
    queryset = MenuOfTheDay.objects.all()
    serializer_class = MenuOfTheDaySerializer
