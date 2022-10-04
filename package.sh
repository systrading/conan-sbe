#!/bin/bash

conan create . --build=missing && \
  conan upload -c "*" --confirm --all --remote staconan
