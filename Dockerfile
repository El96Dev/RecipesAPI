FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /recipes_api

COPY ./requirements.txt /recipes_api/requirements.txt
COPY ./recipes_api /recipes_api

RUN pip install --no-cache-dir --upgrade -r /recipes_api/requirements.txt

