FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /recipes

COPY ./requirements.txt /recipes/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /recipes/requirements.txt

# COPY ./recipes_api /code/recipes_api

# WORKDIR /code/recipes_api

# CMD ["bash", "runscript.sh"]
