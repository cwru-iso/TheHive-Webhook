#!/usr/bin/env bash
# Rebuild image to make sure latest packages are downloaded
cd docker
docker build . -t thehive-lambda-layers --no-cache
cd ..

# Run one-off command to copy new Zips to host
docker run --rm -it -v "$PWD":/app thehive-lambda-layers bash -c ' yes | cp -rf /var/task/*.zip /app'