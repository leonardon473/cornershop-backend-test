# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.conf import settings

from slack_sdk import WebClient

# Project libs

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Dict, List

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

client = WebClient(token=settings.SLACK_BOT_TOKEN)

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


def get_all_members_data_in_the_workspace() -> "List[Dict[str, Any]]":
    result = client.users_list()

    return [
        {"id": m["id"], "name": m["real_name"]}
        for m in result.data["members"]
        if ["is_email_confirmed"]
    ]


def send_message_to_all_workspace_users(message: str):
    result = client.users_list()
    member: "Dict[str, Any]"
    for member in result.data["members"]:
        if member["is_email_confirmed"]:
            result = client.chat_postMessage(channel=member["id"], text=message)


def send_message_to_slack_user(message: str, member_id: str):
    client.chat_postMessage(channel=member_id, text=message)
