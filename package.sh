#!/bin/bash

conan create . --build=missing -pr:b=default -pr:h=default
conan upload -c "*" --all --remote staconan --force
