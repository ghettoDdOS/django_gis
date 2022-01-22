from django.urls import path, re_path

from .views import BuildingViewsetAPI

app_name = "city_map"

urlpatterns = [
    path(
        "",
        BuildingViewsetAPI.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:pk>/",
        BuildingViewsetAPI.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    re_path(
        r"^",
        BuildingViewsetAPI.as_view(
            {
                "get": "list",
            }
        ),
    ),
]
