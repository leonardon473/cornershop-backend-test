from django.urls import path

from .views import menu_of_the_day_admin

urlpatterns = [
    path("admin", menu_of_the_day_admin),
]
