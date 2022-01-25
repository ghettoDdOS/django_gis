import json

from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from ..models import Building

ENDPOINT = reverse("api:v1:city_map:building")
DATASET = [
    {
        "id": 0,
        "address": "red",
        "geom": "POLYGON ((0 0, 0 300, 300 300, 300 0, 0 0))",
    },
    {
        "id": 1,
        "address": "green",
        "geom": "POLYGON ((0 0, 0 50, 50 50, 50 0, 0 0))",
    },
    {
        "id": 2,
        "address": "blue",
        "geom": "POLYGON ((0 0, 0 150, 150 150, 150 0, 0 0))",
    },
    {
        "id": 3,
        "address": "orange",
        "geom": "POLYGON ((0 0, 0 250, 250 250, 250 0, 0 0))",
    },
    {
        "id": 4,
        "address": "pink",
        "geom": "POLYGON ((0 0, 0 350, 350 350, 350 0, 0 0))",
    },
]


class DistanceFiltersTest(APITestCase):
    def setUp(self):
        Building.objects.bulk_create([Building(**item) for item in DATASET])

    def test_lat_lon_radius_filters(self):
        expected_data = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [0.0, 0.0],
                                [0.0, 50.0],
                                [50.0, 50.0],
                                [50.0, 0.0],
                                [0.0, 0.0],
                            ]
                        ],
                    },
                    "properties": {"id": 1, "address": "green"},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [0.0, 0.0],
                                [0.0, 150.0],
                                [150.0, 150.0],
                                [150.0, 0.0],
                                [0.0, 0.0],
                            ]
                        ],
                    },
                    "properties": {"id": 2, "address": "blue"},
                },
            ],
        }

        lat = 30
        lon = 25
        radius = 5

        uri = "%s?lat=%i&lon=%i&radius=%i" % (
            ENDPOINT,
            lat,
            lon,
            radius,
        )

        response = self.client.get(
            uri,
            format="geojson",
            content_type="application/vnd.geo+json",
        )

        response.render()
        data = json.loads(response.content)

        self.assertDictEqual(data, expected_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
