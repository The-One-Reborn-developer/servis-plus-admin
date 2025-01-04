#!/bin/bash

cd "$(dirname "$0")/.."

# Bring down the existing dev timer runner environment
sudo docker-compose -p dev -f dockerfiles/docker-compose-timer-runner-dev.yml down -v

# Build the dev timer runner images
sudo docker-compose -p dev -f dockerfiles/docker-compose-timer-runner-dev.yml build

# Bring up the dev timer runner environment
sudo docker-compose -p dev -f dockerfiles/docker-compose-timer-runner-dev.yml up
