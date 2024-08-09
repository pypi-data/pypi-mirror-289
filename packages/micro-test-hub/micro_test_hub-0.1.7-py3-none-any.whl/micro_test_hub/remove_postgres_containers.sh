#!/bin/bash

# Get the list of exited containers with names containing "hub-postgres"
containers=$(docker ps -a --filter "status=exited" | grep hub-postgres | awk '{print $1}')

# Loop through each container ID and remove it
for container in $containers; do
    docker rm $container
done