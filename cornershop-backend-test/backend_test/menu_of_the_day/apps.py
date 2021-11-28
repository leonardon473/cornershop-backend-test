from django.apps import AppConfig


class MenuOfTheDayConfig(AppConfig):
    name = "backend_test.menu_of_the_day"

    def ready(self):
        from . import tasks  # noqa
