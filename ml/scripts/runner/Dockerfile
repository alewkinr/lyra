# Аргументы для сборки
ARG REGISTRY="docker.pkg.github.com/alewkinr/lyra"
ARG MODEL_NAME
ARG VERSION="latest"

FROM docker.pkg.github.com/alewkinr/lyra/$MODEL_NAME:$VERSION as model


# образ раннера (который запускает и крутит модели)
FROM $REGISTRY/runner:latest

COPY --from=model /model /service/model

RUN  pip install -r /service/requirements.txt

CMD ["python", "/service/main.py"]



