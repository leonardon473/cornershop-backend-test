from ..envtools import getenv

BACKEND_HOST = getenv("BACKEND_HOST")
if not BACKEND_HOST.endswith("/"):
    BACKEND_HOST = BACKEND_HOST + "/"
