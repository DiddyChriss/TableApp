FROM python:3.10.12

RUN apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/*
RUN pip install -U pip && apt-get update
RUN pip install poetry
ENV PATH="${PATH}:/root/.poetry/bin"

ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/tablebuilder

ENV APPLICATION_DIR=/usr/src/tablebuilder

RUN mkdir $APPLICATION_DIR/static
RUN mkdir $APPLICATION_DIR/media

WORKDIR $APPLICATION_DIR

COPY pyproject.toml $APPLICATION_DIR
COPY poetry.lock $APPLICATION_DIR
COPY scripts/create_superuser.sh $APPLICATION_DIR/scripts/create_superuser.sh

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root

COPY . $APPLICATION_DIR
