FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /service
WORKDIR /service
RUN pip install -r requirements.txt

ENV PYTHONPATH=/service

WORKDIR /service/model

EXPOSE 8080
ENTRYPOINT ["python", "main.py"]
