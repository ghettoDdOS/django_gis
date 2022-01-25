from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path(
        "city-map/",
        include("apps.api.city_map.v1"),
    ),
]
