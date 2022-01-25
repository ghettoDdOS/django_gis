from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from apps.core.utils.parsers import GeoJSONParser
from apps.core.utils.renderers import GeoJSONRenderer

from ..filters import filter_by_area, filter_by_distance
from ..models import Building
from .serializers import BuildingSerializer


class BuildingViewsetAPI(ModelViewSet):
    renderer_classes = [
        GeoJSONRenderer,
        JSONRenderer,
        BrowsableAPIRenderer,
    ]
    parser_classes = [GeoJSONParser, JSONParser]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        queryset = super().get_queryset()

        query_params = self.request.query_params
        if query_params:
            min_area = query_params.get("min_area", None)
            max_area = query_params.get("max_area", None)
            queryset = filter_by_area(queryset, min_area, max_area)

            lat = query_params.get("lat", None)
            lon = query_params.get("lon", None)
            radius = query_params.get("radius", None)
            queryset = filter_by_distance(queryset, lat, lon, radius)

        return queryset

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "min_area",
                openapi.IN_QUERY,
                description="Минимальная площадь",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "max_area",
                openapi.IN_QUERY,
                description="Максимальная площадь",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "lat",
                openapi.IN_QUERY,
                description="Широта",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "lon",
                openapi.IN_QUERY,
                description="Долгота",
                type=openapi.TYPE_NUMBER,
            ),
            openapi.Parameter(
                "radius",
                openapi.IN_QUERY,
                description="Радиус",
                type=openapi.TYPE_NUMBER,
            ),
        ],
    )
    def list(self, *args, **kwargs):
        """Список всех строений FeaturesCollection в формате GeoJSON"""
        self.many = True
        return super().list(*args, **kwargs)

    def create(self, *args, **kwargs):
        """Создать новую запись. Ожидается Feature в формате GeoJSON"""
        return super().create(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        """Получить строение по id Feature в формате GeoJSON"""
        return super().retrieve(*args, **kwargs)

    def update(self, *args, **kwargs):
        """Обновить строение по id Feature в формате GeoJSON"""
        return super().update(*args, **kwargs)

    def destroy(self, *args, **kwargs):
        """Удалить строение по id"""
        return super().destroy(*args, **kwargs)

    def partial_update(self, *args, **kwargs):
        """Частично обновить строение по id Feature в формате GeoJSON"""
        return super().partial_update(*args, **kwargs)
