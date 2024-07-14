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

# Delete frontend code

# Define the directories and the files to keep
folders2=(
    "generator_output/vue-template/src/service/"
	"generator_output/vue-template/src/components/"
)
files_to_keep=(
	"api.js"
) # Add more files to this array if needed

# Loop through each directory in folders2
for service_directory in "${folders2[@]}"; do
    if [ -d "$service_directory" ]; then
        # Loop through each item in the directory
        for item in "$service_directory"/*; do
            keep=false
            for file in "${files_to_keep[@]}"; do
                if [ "$(basename "$item")" == "$file" ]; then
                    keep=true
                    break
                fi
            done

            if [ "$keep" = false ]; then
                if [ -d "$item" ]; then
                    echo "Deleting directory: $item"
                    rm -rf "$item"
                elif [ -f "$item" ]; then
                    echo "Deleting file: $item"
                    rm -f "$item"
                fi
            else
                echo "Keeping file: $item"
            fi
        done
    else
        echo "Directory not found: $service_directory"
    fi
done

echo "Deletion complete."