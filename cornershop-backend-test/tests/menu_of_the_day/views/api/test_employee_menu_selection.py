from typing import cast

import pytest
from rest_framework.test import APIClient

from model_bakery import baker

from backend_test.menu_of_the_day.models import EmployeeMenuSelection, FoodDish

pytestmark = pytest.mark.django_db


class TestEmployeeMenuSelectionRetrieveUpdateView:

    endpoint = "/menu/api/employee-menu-selections"

    def setup_method(self, method):
        self.api_client = APIClient()
        self.selection = cast(EmployeeMenuSelection, baker.make(EmployeeMenuSelection))
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
        from pprint import pprint

        pprint(data)
        assert response.status_code == 200
        assert data == expected_json

    def test_update(self):
        # Arrange
        update_dict = {"selected_food_dish": self.food_dish.id}
        url = f"{self.endpoint}/{self.selection.id}"

        # Act
        response = self.api_client.put(url, update_dict, format="json")

        # Assert
        self.selection.refresh_from_db()
        # remove field with unpredictable value
        assert response.status_code == 200
        assert self.selection.selected_food_dish.id == self.food_dish.id

    @pytest.mark.parametrize(
        "field",
        [
            ("food_dish"),
        ],
    )
    def test_partial_update(self, field: str):
        # Arrange
        update_dict = {"food_dish": self.food_dish.id}
        valid_field = update_dict[field]
        url = f"{self.endpoint}/{self.selection.id}"

        # Act
        response = self.api_client.patch(url, {field: valid_field}, format="json")

        # Assert
        assert response.status_code == 200
