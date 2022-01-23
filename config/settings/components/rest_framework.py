"""Rest framework settings"""

DATE_INPUT_FORMATS = [
    ("%d-%m-%Y"),
    ("%d.%m.%Y"),
    ("%d/%m/%Y"),
    "iso-8601",
]


REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        # "apps.core.api.permissions.HasApiKeyOrIsAdmin",
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DATE_FORMAT": "%d/%m/%Y",
    "DATE_INPUT_FORMATS": DATE_INPUT_FORMATS,
    "DATETIME_FORMAT": "%d/%m/%Y %H:%M",
}
SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
}
