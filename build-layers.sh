#!/usr/bin/env bash
PYTHON_VERSION=3.7
BUILD_TAG=thehive-lambda-layers

# Rebuild image to make sure latest packages are downloaded
echo "======== Pulling base docker image ========"
docker pull "lambci/lambda:build-python$PYTHON_VERSION"

echo "======== Building docker image ========"
cd docker
docker build . -t "$BUILD_TAG" --build-arg PYTHON_VERSION --no-cache
cd ..

# Run one-off command to copy new Zips to host
echo "======== Copying completed layer builds to host ========"
docker run --rm -it -v "$PWD":/app "$BUILD_TAG" bash -c ' yes | cp -rvf /var/task/*.zip /app'

# Cleanup dangling images
echo "======== Cleaning up dangling docker images ========"
docker rmi $(docker images -f "dangling=true" -q) 2>/dev/null
