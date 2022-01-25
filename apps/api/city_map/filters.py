from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework.exceptions import APIException


def filter_by_area(queryset, min_area=None, max_area=None):
    if min_area:
        queryset = [item for item in queryset if item.area > float(min_area)]

    if max_area:
        queryset = [item for item in queryset if item.area < float(max_area)]

    return queryset


def filter_by_distance(queryset, lat=None, lon=None, radius=None):
    if all([lat, lon, radius]):
        queryset = queryset.filter(
            geom__distance_lte=(
                Point(float(lat), float(lon)),
                D(m=float(radius)),
            )
        )
    elif any([lat, lon, radius]):
        raise APIException(
            "Для использования фильтра по радиусу необходимо"
            + " задать все три параметра(lat, lon, radius)",
        )
    return queryset
