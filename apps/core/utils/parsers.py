import json

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos.error import GEOSException
from rest_framework.exceptions import ParseError
from rest_framework.parsers import JSONParser


class GeoJSONParser(JSONParser):
    media_type = "application/vnd.geo+json"

    def parse(self, stream, *args, **kwargs):
        data = super().parse(stream, *args, **kwargs)
        assert data["type"] == "Feature", "Ожидался Feature в формате GeoJSON"

        geometry_field = getattr(
            args[1].get("view").serializer_class.Meta, "geometry_field", None
        )
        assert (
            geometry_field
        ), "Необходимо явно указать геометрическое поле в сериализаторе!"

        try:
            output = {
                **data.get("properties", {}),
                geometry_field: GEOSGeometry(json.dumps(data["geometry"])),
            }
        except GEOSException as error:
            raise ParseError(error)

        return output