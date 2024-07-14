#!/bin/bash

# Define the folders to be deleted
folders=(
    "generator_output/backend-service/src/main/java/ftn/backendservice/controllers/"
    "generator_output/backend-service/src/main/java/ftn/backendservice/domain/"
    "generator_output/backend-service/src/main/java/ftn/backendservice/repositories/"
    "generator_output/backend-service/src/main/java/ftn/backendservice/services/"
)

# Loop through each folder and delete it
for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "Deleting folder: $folder"
        rm -rf "$folder"
    else
        echo "Folder not found: $folder"
    fi
done

echo "Deletion complete."