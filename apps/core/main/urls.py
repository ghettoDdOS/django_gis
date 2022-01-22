from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="api/")),
    path("api/", include("apps.core.api.urls"), name="api"),
]
