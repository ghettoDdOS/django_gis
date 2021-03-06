from django.template.loader import render_to_string
from django.templatetags.static import static
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SchemaView = get_schema_view(
    openapi.Info(
        title=_("API"),
        default_version="v1",
        description=render_to_string("api/desctiption.html"),
        contact=openapi.Contact(email="example@example.com"),
        license=openapi.License(name="MIT License"),
        x_logo={
            "url": static("images/logo.png"),
            "altText": _("Логотип"),
            "href": "/",
            "backgroundColor": "transparent",
        },
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path("api/", include("apps.core.api.urls")),
    ],
)
