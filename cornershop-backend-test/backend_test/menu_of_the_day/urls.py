from django.urls import include, path

from .views.api import (
    EmployeeMenuSelectionRetrieveUpdateView,
    MenuOfTheDayListCreateApiView,
    MenuOfTheDayRetrieveUpdateDestroyView,
)
from .views.html import (
    employee_menu_selection_retrieve_update_view,
    menu_of_the_day_list_create,
    menu_of_the_day_retrieve_update_destroy,
    user_login_view,
)

admin_urlpatterns = (
    [
        path("login", user_login_view, name="login"),
        path("menus", menu_of_the_day_list_create, name="menu-listing"),
        path("menus/<int:id>", menu_of_the_day_retrieve_update_destroy),
    ],
    "admin",
)

urlpatterns = [
    path(
        "<uuid:id>",
        employee_menu_selection_retrieve_update_view,
    ),
    path("admin/", include(admin_urlpatterns)),
    path("admin/api/menus", MenuOfTheDayListCreateApiView.as_view()),
    path("admin/api/menus/<int:pk>", MenuOfTheDayRetrieveUpdateDestroyView.as_view()),
    path(
        "api/employee-menu-selections/<uuid:pk>",
        EmployeeMenuSelectionRetrieveUpdateView.as_view(),
    ),
]
