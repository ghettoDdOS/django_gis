import json

from django.contrib.gis.geos import GEOSGeometry
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList


class GeoJSONRenderer(JSONRenderer):
    format = "geojson"
    media_type = "application/vnd.geo+json"

    def render(self, data, *args, **kwargs):
        view = args[1].get("view")
        many = getattr(view, "many", False)
        meta_data = view.serializer_class.Meta
        fields = getattr(meta_data, "fields", None)
        geometry_field = getattr(meta_data, "geometry_field", None)
        assert geometry_field, (
            "Необходимо явно указать геометрическое поле(geometry_field)"
            + "в Meta классе сериализатора!"
        )

        if not isinstance(data, ReturnList):
            data = [data]

        try:
            features = [
                {
                    "type": "Feature",
                    "geometry": json.loads(
                        GEOSGeometry(item.pop(geometry_field)).geojson
                    ),
                    "properties": {
                        key: value
                        for key, value in item.items()
                        if key in fields or not fields
                    },
                }
                for item in data
            ]
        except Exception:
            return super().render(*data, *args, **kwargs)

        if many:
            data = {"type": "FeatureCollection", "features": features}
        else:
            data = features[0]

        return super().render(data, *args, **kwargs)
