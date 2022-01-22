from django.contrib.gis.geos import Polygon
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Building


class BuildingSerializer(serializers.ModelSerializer):
    def validate_geom(self, poly: Polygon):
        if not poly.valid:
            raise ValidationError(
                "Неверная геометрическая фигура: %s" % poly.valid_reason
            )

        return poly

    class Meta:
        model = Building
        geometry_field = "geom"
        fields = ("id", "address", "geom")
