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
    libffi-dev \
    curl \
    jpeg-dev \
    zlib-dev \
    musl-dev \
    gcc \
    gdk-pixbuf-dev \
    python3-dev \
    make \
    gdal

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="${PATH}:/root/.poetry/bin"

# install backend packages
COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN set -ex && poetry install --no-root

COPY . .

RUN ["chmod", "+x", "/var/www/app/wait-for"]
