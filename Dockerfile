FROM python:3.8.11-alpine

WORKDIR /var/www/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install global packages
RUN apk update\
    && apk upgrade \
    && apk add --no-cache  \
    git \
    postgresql-dev \
    bash \
    libc-dev \
    curl \
    gcc \
    cairo-dev \
    python3-dev \
    gdk-pixbuf-dev  \
    make \
    gdal \
    gdal-dev \
    geos \
    geos-dev

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

# install backend packages
COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN set -ex && poetry install --no-root

COPY . .

RUN ["chmod", "+x", "/var/www/app/wait-for"]
