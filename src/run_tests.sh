#!/bin/bash

./setup_contracts.sh /home/owen/Documents/GitHub/GPTScan-Bigger-Model/data/test

# Define the directory and the main script path
test_directory="/home/owen/Documents/GitHub/GPTScan-Bigger-Model/data/test"
main_script_path="main.py"

# Iterate over all directories in the test directory
for dir_path in "$test_directory"/*; do
    # Ensure it's a directory
    if [[ -d "$dir_path" ]]; then
        # Construct and execute the command
        echo "Running command: python3 $main_script_path -s $dir_path"
        python3 "$main_script_path" -s "$dir_path"

        # Check if the command failed
        if [[ $? -ne 0 ]]; then
            echo "Error while running command for directory: $dir_path"
        fi
    fi
done
