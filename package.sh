#!/bin/bash

image=092165354856.dkr.ecr.ap-southeast-2.amazonaws.com/symbio-devtools:latest

eval $(aws ecr get-login --region ap-southeast-2 | sed -e 's/-e none//g')

docker run -v${PWD}:/app:Z ${image} \
  conan create /app && \
  conan upload -c "*" --remote staconan --force

