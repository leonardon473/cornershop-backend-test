from backend_test.menu_of_the_day.integrations.slack import (
    get_all_members_data_in_the_workspace,
)

from .payload_get_all_members_data_in_the_workspace import CLIENT_USERS_LIST_RETURN_DATA


class TestGetAllMembersDataInTheWorkspace:
    def test_returned_data_based_on_api_example_data(self, mocker):
        # Arrange
        result = mocker.Mock()
        result.data = CLIENT_USERS_LIST_RETURN_DATA
        mocker.patch(
            "backend_test.menu_of_the_day.integrations.slack.client.users_list",
            return_value=result,
        )

        # Act
        returned = get_all_members_data_in_the_workspace()
        # Assert
        assert returned == [{"id": "U02P409RTUG", "name": "Leonardo Ramírez"}]
