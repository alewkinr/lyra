# определяем registry
ENV REGISTRY="docker.pkg.github.com/alewkinr/lyra"

# Аргументы для сборки
ARG MODEL_NAME
ARG VERSION="latest"

# базовый образ с моделью внутри
FROM $REGISTRY/$MODEL_NAME:$VERSION as model

# образ раннера (который запускает и крутит модели)
FROM $REGISTRY/runner:latest

COPY --from=model /model /service/model

CMD ["python", "-c", "main.py"]



