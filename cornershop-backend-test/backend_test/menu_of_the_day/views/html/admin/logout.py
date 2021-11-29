from typing import TYPE_CHECKING

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


def logout_view(request: "HttpRequest") -> "HttpResponse":
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
