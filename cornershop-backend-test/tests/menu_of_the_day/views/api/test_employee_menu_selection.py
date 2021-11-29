from datetime import date, time
from typing import cast

import pytest
from django.test import override_settings
from rest_framework.test import APIClient

from freezegun import freeze_time
from model_bakery import baker

from backend_test.menu_of_the_day.models import EmployeeMenuSelection, FoodDish

pytestmark = pytest.mark.django_db


class TestEmployeeMenuSelectionRetrieveUpdateView:

    endpoint = "/menu/api/employee-menu-selections"

    def setup_method(self, method):
        self.api_client = APIClient()
        self.selection = cast(
            EmployeeMenuSelection,
            baker.make(
                EmployeeMenuSelection,
                menu_of_the_day__date=date(2021, 11, 24),
            ),
        )
        self.food_dish = cast(
            FoodDish,
            baker.make(
                FoodDish, menu_of_the_day=self.selection.menu_of_the_day, food="Tacos"
            ),
        )

    def test_retrieve(self):
        # Arrange
        expected_json = {
            "employee": {"name": self.selection.employee.name},
            "food_dish_customization": "",
            "menu_of_the_day": {
                "date": self.selection.menu_of_the_day.date.strftime("%Y-%m-%d"),
                "food_dishes": [{"food": self.food_dish.food, "id": self.food_dish.id}],
            },
            "selected_food_dish_id": self.selection.selected_food_dish_id,
        }

        url = f"{self.endpoint}/{self.selection.id}"

        # Act
        response = self.api_client.get(url)

        # Assert
        data = response.json()

        assert response.status_code == 200
        assert data == expected_json

    @freeze_time("2021-11-24 09:00 -04:00")
    @override_settings(TIME_LIMIT_TO_ORDER=time(11, 0))
    def test_update(self):
        # Arrange
        update_dict = {
            "selected_food_dish": self.food_dish.id,
            "food_dish_customization": "Without salt",
        }
        url = f"{self.endpoint}/{self.selection.id}"

        # Act
        response = self.api_client.put(url, update_dict, format="json")

        # Assert
        self.selection.refresh_from_db()

        assert response.status_code == 200
        assert self.selection.selected_food_dish.id == self.food_dish.id
        assert self.selection.food_dish_customization == "Without salt"
