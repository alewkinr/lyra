FROM python:3.7
# todo: create custom base image

COPY . /service
COPY data /data
WORKDIR /service

RUN pip install -r requirements.txt

