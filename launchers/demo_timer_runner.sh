#!/bin/bash

cd "$(dirname "$0")/.."

# Bring down the existing demo_timer_runner environment
sudo docker-compose -p demo_timer_runner -f dockerfiles/docker-compose-timer-runner-demo.yml down -v

# Build the demo_timer_runner images
sudo docker-compose -p demo_timer_runner -f dockerfiles/docker-compose-timer-runner-demo.yml build

# Bring up the demo_timer_runner environment
sudo docker-compose -p demo_timer_runner -f dockerfiles/docker-compose-timer-runner-demo.yml up -d
