#! /usr/bin/env sh

# Exit in case of error
set -e

REGISTRY="docker.pkg.github.com/alewkinr/lyra"
MODEL=$1
VERSION=$2
TAG=$3


if [ -z "$TAG" ]; then
    TAG="undefined"
fi

# for now all images saves in ml/bin directory
docker build ./runner --build-arg MODEL_NAME=$MODEL --build-arg VERSION=$VERSION -t $REGISTRY/$MODEL
docker tag $REGISTRY/$MODEL $REGISTRY/$MODEL:$TAG && docker push $REGISTRY/$MODEL:$TAG


