FROM python:3.7

COPY . /service
WORKDIR /service
RUN pip install -r requirements.txt

ENV PYTHONPATH=/service

WORKDIR /service/auth
ENTRYPOINT ["python", "main.py"]
