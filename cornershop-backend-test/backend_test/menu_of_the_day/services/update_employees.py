from backend_test.menu_of_the_day.integrations.slack import (
    get_all_members_data_in_the_workspace,
)
from backend_test.menu_of_the_day.models import Employee


def update_emplooyes_from_slack():
    slack_members = get_all_members_data_in_the_workspace()
    for member in slack_members:
        Employee.objects.get_or_create(
            slack_id=member["id"],
            defaults={
                "name": member["name"],
            },
        )
