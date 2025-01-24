#!/bin/bash

cd "$(dirname "$0")/.."

# Bring down the existing demo_admin environment
sudo docker-compose -p demo_admin -f dockerfiles/docker-compose-demo.yml down -v

# Build the demo_admin images
sudo docker-compose -p demo_admin -f dockerfiles/docker-compose-demo.yml build

# Bring up the demo_admin environment
sudo docker-compose -p demo_admin -f dockerfiles/docker-compose-demo.yml up -d
