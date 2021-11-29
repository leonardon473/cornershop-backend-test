# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Project libs

# If type checking, __all__
if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def user_login_view(request: "HttpRequest") -> "HttpResponse":
    if request.method == "POST":
        # Process the request if posted data are available
        username: str = request.POST["username"]
        password: str = request.POST["password"]
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(
                request,
                "registration/login.html",
                {"error_message": "Usuario o contraseña incorrectos."},
            )
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, "registration/login.html")
