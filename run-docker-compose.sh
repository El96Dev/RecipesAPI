#!/bin/bash

# Build the Docker containers
echo "Building Docker containers..."
docker compose -f docker-compose.yml build --no-cache

# Check if the build was successful
if [ $? -eq 0 ]; then
  echo "Build successful. Starting containers..."
  docker compose -f docker-compose.yml up
else
  echo "Build failed. Exiting..."
  exit 1
fi