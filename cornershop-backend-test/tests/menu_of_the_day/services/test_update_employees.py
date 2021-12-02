import pytest

from model_bakery import baker

from backend_test.menu_of_the_day.models import Employee
from backend_test.menu_of_the_day.services.update_employees import (
    update_emplooyes_from_slack,
)

pytestmark = pytest.mark.django_db


class TestUpdateEmployeesService:
    def test_one_employee_is_added(self, mocker):
        # Arrange
        mocker.patch(
            "backend_test.menu_of_the_day.services.update_employees.get_all_members_data_in_the_workspace",
            return_value=[{"id": 1, "name": "Leonardo Ramírez"}],
        )
        old_employees_count = Employee.objects.count()

        # Act
        update_emplooyes_from_slack()

        # Assert
        assert Employee.objects.count() == old_employees_count + 1

    def test_two_employees_are_added(self, mocker):
        # Arrange
        mocker.patch(
            "backend_test.menu_of_the_day.services.update_employees.get_all_members_data_in_the_workspace",
            return_value=[
                {"id": 1, "name": "Leonardo Ramírez"},
                {"id": 2, "name": "Omar Genaro"},
            ],
        )
        old_employees_count = Employee.objects.count()

        # Act
        update_emplooyes_from_slack()
        # Assert
        assert Employee.objects.count() == old_employees_count + 2

    def test_update_twice_do_not_duplicate_data(self, mocker):
        # Arrange
        mocker.patch(
            "backend_test.menu_of_the_day.services.update_employees.get_all_members_data_in_the_workspace",
            return_value=[
                {"id": 1, "name": "Leonardo Ramírez"},
                {"id": 2, "name": "Omar Genaro"},
            ],
        )
        old_employees_count = Employee.objects.count()

        # Act
        update_emplooyes_from_slack()
        update_emplooyes_from_slack()

        # Assert
        assert Employee.objects.count() == old_employees_count + 2

    def test_update_adds_differences_between_old_data_and_the_new(self, mocker):
        # Arrange
        baker.make(Employee, slack_id=1)
        baker.make(Employee, slack_id=2)
        mocker.patch(
            "backend_test.menu_of_the_day.services.update_employees.get_all_members_data_in_the_workspace",
            return_value=[
                {"id": 1, "name": "Leonardo Ramírez"},
                {"id": 2, "name": "Omar Genaro"},
                {"id": 3, "name": "Edgar Alan"},
            ],
        )
        old_employees_count = Employee.objects.count()

        # Act
        update_emplooyes_from_slack()

        # Assert
        assert Employee.objects.count() == old_employees_count + 1
