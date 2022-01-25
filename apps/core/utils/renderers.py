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

        if not data:
            return super().render(data, *args, **kwargs)

        if not isinstance(data, ReturnList):
            data = [data]

        features = []
        for item in data:
            try:
                geometry = json.loads(
                    GEOSGeometry(item.pop(geometry_field), srid=4326).geojson
                )
            except Exception:
                geometry = {}
            features.append(
                {
                    "type": "Feature",
                    "geometry": geometry,
                    "properties": {
                        key: value
                        for key, value in item.items()
                        if key in fields or not fields
                    },
                }
            )

        if many:
            data = {"type": "FeatureCollection", "features": features}
        else:
            data = features[0]
        return super().render(data, *args, **kwargs)
