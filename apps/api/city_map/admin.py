from django.contrib.gis.admin import OSMGeoAdmin, register

from .models import Building


@register(Building)
class BuildingAdmin(OSMGeoAdmin):
    list_display = (
        "id",
        "address",
    )
