FROM python:3.7

COPY ./requirements.txt /api/requirements.txt

WORKDIR /api
RUN pip install -r requirements.txt

COPY . /api

EXPOSE 8000