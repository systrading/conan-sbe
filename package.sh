#!/bin/bash

conan create . 
conan upload -c "sbe*" --remote staconan --force
