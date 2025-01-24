#!/bin/bash

cd "$(dirname "$0")/.."

# Bring down the existing dev_admin environment
sudo docker-compose -p dev_admin -f dockerfiles/docker-compose-dev.yml down -v

# Build the dev_admin images
sudo docker-compose -p dev_admin -f dockerfiles/docker-compose-dev.yml build

# Bring up the dev_admin environment
sudo docker-compose -p dev_admin -f dockerfiles/docker-compose-dev.yml up
