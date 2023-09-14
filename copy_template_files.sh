#!/bin/bash

# Source directory
source_dir="airbyte_connection_templates"

# Destination directory
destination_dir="octavia/"

airbyte_configuration_types=("sources" "destinations" "connections")

string_list=("String1" "String2" "String3")

for connection_type in "${airbyte_configuration_types[@]}"; do
    for source_file in "$source_dir"/"$connection_type"/*.yaml; do
        # Get the filename (without the path)
        filename=$(basename "$source_file")

        # Create the destination directory (if it doesn't exist)
        mkdir -p "$destination_dir/$connection_type/$filename"

        # Copy the source file to the destination with the desired name
        cp "$source_file" "$destination_dir/$connection_type/$filename/configuration.yaml"
    done
done

echo "Files copied successfully."
