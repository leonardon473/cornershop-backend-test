import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from backend_test.menu_of_the_day.models import MenuOfTheDay

pytestmark = pytest.mark.django_db


class TestMenuOfTheDayListCreateView:

    endpoint = "/menu/admin/api/menus"

    def test_list_menus_with_one_item(self):
        # Arrange
        api_client = APIClient()
        baker.make(MenuOfTheDay)

        # Act
        response = api_client.get(self.endpoint)

        # Assert
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 1
        assert isinstance(data[0], dict)

    def test_create(self):
        # Arrange
        api_client = APIClient()
        payload = {
            "date": "2021-11-24",
            "food_dishes": [{"food": "Chicken"}, {"food": "Tacos"}],
        }
        old_obj_count = MenuOfTheDay.objects.count()

        # Act
        response = api_client.post(self.endpoint, data=payload, format="json")

        # Assert
        data = response.json()
        assert response.status_code == 201
        assert isinstance(data, dict)
        assert MenuOfTheDay.objects.count() == old_obj_count + 1

    def test_retrieve(self):
        # Arrange
        api_client = APIClient()
        menu = baker.make(MenuOfTheDay)
        expected_json = {
            "date": menu.date.strftime("%Y-%m-%d"),
            "food_dishes": [],
        }
        url = f"{self.endpoint}/{menu.id}"

        # Act
        response = api_client.get(url)

        # Assert
        data = response.json()
        del data["id"]
        assert response.status_code == 200
        assert data == expected_json

    def test_update(self):
        # Arrange
        api_client = APIClient()
        menu = baker.make(MenuOfTheDay)
        update_dict = {"date": "2021-11-24", "food_dishes": [{"food": "Tacos"}]}

        url = f"{self.endpoint}/{menu.id}"

        # Act
        response = api_client.put(url, update_dict, format="json")

        # Assert
        data = response.json()
        # remove field with unpredictable value
        del data["id"]
        del data["food_dishes"][0]["id"]
        assert response.status_code == 200
        assert data == update_dict

    @pytest.mark.parametrize(
        "field",
        [
            ("date"),
            ("food_dishes"),
        ],
    )
    def test_partial_update(self, field: str):
        # Arrange
        api_client = APIClient()
        menu = baker.make(MenuOfTheDay)
        menu_dict = {"date": "2021-11-24", "food_dishes": [{"food": "Tacos"}]}
        valid_field = menu_dict[field]
        url = f"{self.endpoint}/{menu.id}"

        # Act
        response = api_client.patch(url, {field: valid_field}, format="json")

        # Assert
        data = response.json()
        del data["id"]
        try:  # the field to delete can not be available in some cases
            del data[field][0]["id"]  # remove field with unpredictable value
        except TypeError:
            pass
        assert response.status_code == 200
        assert data[field] == valid_field

    def test_delete(self):
        api_client = APIClient()
        menu = baker.make(MenuOfTheDay)
        old_menus_count = MenuOfTheDay.objects.count()
        url = f"{self.endpoint}/{menu.id}"

        response = api_client.delete(url)

        assert response.status_code == 204
        assert MenuOfTheDay.objects.count() == old_menus_count - 1
