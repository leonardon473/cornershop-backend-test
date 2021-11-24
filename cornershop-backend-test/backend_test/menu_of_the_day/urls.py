from django.urls import path

from .views.admin import menu_of_the_day_list_create
from .views.api import MenuOfTheDayListApiView

urlpatterns = [
    path("admin", menu_of_the_day_list_create),
    path("admin/api/menus", MenuOfTheDayListApiView.as_view()),
]
