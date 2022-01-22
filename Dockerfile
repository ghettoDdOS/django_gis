FROM python:3.8.11-alpine

WORKDIR /app/
# ENV HOME=/root/

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
    gdal \
    gdal-dev \
    geos \
    geos-dev

# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
# ENV PATH="${PATH}:/root/.poetry/bin"

# install backend packages
COPY requirements.txt requirements.txt
# COPY pyproject.toml pyproject.toml
# COPY poetry.lock poetry.lock
RUN set -ex && pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "/app/wait-for"]
