import json

from django.contrib.gis.geos import GEOSGeometry
from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnList

from .gis import is_geometry


class GeoJSONRenderer(JSONRenderer):
    charset = "utf-8"
    media_type = "application/vnd.geo+json"

    def render(self, data, *args, **kwargs):
        print(GEOSGeometry(data[0]["geom"]).geojson)
        meta_data = args[1].get("view").serializer_class.Meta
        instance = meta_data.model
        geometry_field = getattr(meta_data, "geometry_field", None)
        assert (
            geometry_field
        ), "Необходимо явно указать геометрическое поле в сериализаторе!"

        fields = getattr(
            meta_data,
            "fields",
            [
                field.name
                for field in instance._meta.fields
                if field.name != geometry_field
            ],
        )

        if isinstance(data, dict):
            data = [
                data,
            ]

        try:
            output = serialize(
                "geojson",
                [instance(**item) for item in data],
                geometry_field=geometry_field,
                fields=fields,
            )
        except TypeError:
            return super().render(data)

        if len(data) == 1:
            output = json.dumps(json.loads(output)["features"][0])

        return output.encode(self.charset)


class TestGeoJSONRenderer(JSONRenderer):
    media_type = "application/vnd.geo+json"

    def render(self, data, *args, **kwargs):
        features = []
        if not isinstance(data, ReturnList):
            data = [data]

        for item in data:
            feature = {
                "type": "Feature",
                "geometry": None,
                "properties": {},
            }
            for key, value in item.items():
                if is_geometry(value):
                    feature["geometry"] = json.loads(
                        GEOSGeometry(value).geojson
                    )
                else:
                    feature["properties"].update({key: value})
            features.append(feature)
        count_of_features = len(features)
        if count_of_features > 1:
            data = {"type": "FeatureCollection", "features": features}
        elif count_of_features == 1:
            data = features[0]
        else:
            data = ""

        return super().render(data, *args, **kwargs)
