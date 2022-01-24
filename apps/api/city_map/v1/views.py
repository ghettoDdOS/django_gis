from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from apps.core.utils.parsers import GeoJSONParser
from apps.core.utils.renderers import GeoJSONRenderer

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
        query_params = self.request.query_params
        queryset = super().get_queryset()

        if "min_area" in query_params:
            min_area = float(query_params["min_area"])
            queryset = [
                building for building in queryset if building.area > min_area
            ]

        if "max_area" in query_params:
            max_area = float(query_params["max_area"])

            queryset = [
                building for building in queryset if building.area < max_area
            ]

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
        ]
    )
    def list(self, *args, **kwargs):
        self.many = True
        return super().list(*args, **kwargs)
