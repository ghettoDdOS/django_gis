from rest_framework.parsers import JSONParser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet

from apps.core.utils.parsers import GeoJSONParser
from apps.core.utils.renderers import TestGeoJSONRenderer

from ..models import Building
from .serializers import BuildingSerializer


class BuildingViewsetAPI(ModelViewSet):
    renderer_classes = [
        TestGeoJSONRenderer,
        JSONRenderer,
        BrowsableAPIRenderer,
    ]
    parser_classes = [GeoJSONParser, JSONParser]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        # query_params = self.request.query_params
        queryset = super().get_queryset()

        # if query_params:
        #     list(
        #         filter(
        #             lambda building: building.geom.area
        #             > int(query_params.get("min", 0))
        #             and building.geom.area
        #             < int(query_params.get("max", 999999999)),
        #             queryset,
        #         )
        #     )
        # print(len(queryset))
        # print(query_params)
        return queryset
