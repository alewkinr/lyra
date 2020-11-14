FROM python:3.7
# todo: create custom base image

#RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

COPY . /service
WORKDIR /service
RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "-c", "sleep 3200"]