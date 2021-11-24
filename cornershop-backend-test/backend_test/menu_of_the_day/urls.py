from django.urls import path

from .views.admin import menu_of_the_day_list_create, menu_of_the_day_retrieve_update_destroy
from .views.api import MenuOfTheDayListCreateApiView, MenuOfTheDayRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/menus", menu_of_the_day_list_create),
    path("admin/menus/<int:id>", menu_of_the_day_retrieve_update_destroy),
    path("admin/api/menus", MenuOfTheDayListCreateApiView.as_view()),
    path("admin/api/menus/<int:pk>",
         MenuOfTheDayRetrieveUpdateDestroyView.as_view()),
]
