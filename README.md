# Django GIS

## Prerequisites

What things you need to install the software and how to install them.

1. Docker
2. docker-compose

## Deployment

A step by step series of examples that tell you how to get a development env running.

1. Create ```.env``` file from ```.env.example``` (just copy it)
2. Run ```docker-compose up``` (port 80 must be free)
3. Open ```localhost/api```

## Test

To run test you need type this(container name may be different).

```zsh
docker exec django_gis_app_1 make test
```

## APP Structure

```
📦apps
 ┗ 📂api
   ┗ 📂city_map
     ┣ 📂migrations
     ┣ 📂tests
     ┃ ┣ 📜area_filters_test.py
     ┃ ┗ 📜distance_filters_test.py
     ┣ 📂v1
     ┃ ┣ 📜routers.py
     ┃ ┣ 📜serializers.py
     ┃ ┗ 📜views.py
     ┣ 📜admin.py
     ┣ 📜apps.py
     ┣ 📜filters.py
     ┣ 📜models.py
     ┗ 📜signals.py
 ```

## API

- POST, PUT Example:
  
```json
{
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          100,
          0
        ],
        [
          101,
          0
        ],
        [
          101,
          1
        ],
        [
          100,
          1
        ],
        [
          100,
          0
        ]
      ]
    ]
  },
  "properties": {
    "address": "Plaz33a Road Park"
  }
}
```

- PATCH Example:

```json
{
  "type": "Feature",
  "properties": {
    "address": "adfa56fdf"
  }
}
```
