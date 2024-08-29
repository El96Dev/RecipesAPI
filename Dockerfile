FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./recipes_api /code/recipes_api

WORKDIR /code/recipes_api

CMD ["bash", "runscript.sh"]
