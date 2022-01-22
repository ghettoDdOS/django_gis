from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CityMapConfig(AppConfig):
    """Default app config"""

    name = "apps.api.city_map"
    verbose_name = _("Карта города")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
