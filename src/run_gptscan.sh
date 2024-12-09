#!/bin/bash

# Check if a directory parameter was provided
if [[ -z "$1" ]]; then
    echo "Usage: $0 <test_directory>"
    exit 1
fi

# Use the provided directory parameter
test_directory="$1"
main_script_path="main.py"
results_dir="/home/owen/Documents/GitHub/GPTScan-Bigger-Model/results/gpt-3.5-turbo/code-423n4-Web3Bugs-data"

# Ensure the results directory exists
mkdir -p "$results_dir"

# Run setup script with the provided directory
./setup_contracts.sh "$test_directory"

# Iterate over all directories in the test directory
for dir_path in "$test_directory"/*; do
    # Ensure it's a directory
    if [[ -d "$dir_path" ]]; then
        # Extract the name of the current directory
        dir_name=$(basename "$dir_path")

        # Define the output file path
        output_file="$results_dir/${dir_name}_results.md"

        # Construct and execute the command, redirecting output to the file
        echo "Running command: python3 $main_script_path -s $dir_path"
        python3 "$main_script_path" -s "$dir_path" | tee "$output_file"

        # Check if the command failed
        if [[ $? -ne 0 ]]; then
            echo "Error while running command for directory: $dir_path" | tee -a "$output_file"
        fi
    fi
done