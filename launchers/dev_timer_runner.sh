#!/bin/bash

cd "$(dirname "$0")/.."

# Bring down the existing dev_timer_runner environment
sudo docker-compose -p dev_timer_runner -f dockerfiles/docker-compose-timer-runner-dev.yml down -v

# Build the dev_timer_runner images
sudo docker-compose -p dev_timer_runner -f dockerfiles/docker-compose-timer-runner-dev.yml build

# Bring up the dev_timer_runner environment
sudo docker-compose -p dev_timer_runner -f dockerfiles/docker-compose-timer-runner-dev.yml up
