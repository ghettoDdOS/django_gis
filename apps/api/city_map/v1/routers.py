from django.urls import path, re_path

from .views import BuildingViewsetAPI

app_name = "city_map"

urlpatterns = [
    re_path(
        r"^building/$",
        BuildingViewsetAPI.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "building/<int:pk>/",
        BuildingViewsetAPI.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
