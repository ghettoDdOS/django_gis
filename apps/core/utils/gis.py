from django.contrib.gis.geos import GEOSGeometry

GEOJSON_TYPES = [
    "Point",
    "LineString",
    "Polygon",
    "MultiPoint",
    "MultiLineString",
    "MultiPolygon",
    "MultiPolygon",
    "FeatureCollection",
    "Feature",
]


def is_geometry(item):
    try:
        GEOSGeometry(item)
    except Exception:
        return False
    return True
