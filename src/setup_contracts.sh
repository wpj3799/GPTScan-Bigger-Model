#!/bin/bash

# Usage: ./script.sh /path/to/parent_directory

# Check if the parent directory is provided
if [ -z "$1" ]; then
    echo "Please provide the parent directory containing the project directories."
    echo "Usage: $0 /path/to/parent_directory"
    exit 1
fi

PARENT_DIR="$1"

# SPDX License Identifier (Change as needed)
SPDX_IDENTIFIER="// SPDX-License-Identifier: MIT"

process_directory() {
    DIR="$1"
    echo "Processing directory: $DIR"

    # Change into the subdirectory
    cd "$DIR" || { echo "Failed to access directory: $DIR"; return; }

    # Initialize npm project
    if [ ! -f "package.json" ]; then
        echo "Initializing npm project in $DIR..."
        yes "" | npm init -y || { echo "npm init failed in $DIR"; return; }
    else
        echo "npm project already initialized in $DIR."
    fi

    # Install Hardhat locally
    echo "Installing Hardhat in $DIR..."
    npm install hardhat --save-dev || { echo "Failed to install Hardhat in $DIR"; return; }

    # Initialize Hardhat with default settings
    if [ ! -f "hardhat.config.js" ]; then
        echo "Initializing Hardhat project in $DIR..."
        yes "" | npx hardhat || { echo "Failed to initialize Hardhat in $DIR"; return; }

        # Delete the default Lock.sol file
        echo "Removing Lock.sol from contracts directory in $DIR..."
        rm -f contracts/Lock.sol || echo "No Lock.sol file found to delete."
    else
        echo "Hardhat already initialized in $DIR."
    fi

    # Move all .sol files in the current directory to the contracts directory
    echo "Moving .sol files to contracts/ in $DIR..."
    mkdir -p contracts
    find . -maxdepth 1 -type f -name "*.sol" -exec mv {} contracts/ \;

    # Extract Solidity versions from .sol files in contracts/ and update hardhat.config.js
    echo "Extracting Solidity versions from .sol files in $DIR..."
    SOLIDITY_VERSIONS=()
    for SOL_FILE in contracts/*.sol; do
        if [ -f "$SOL_FILE" ]; then
            VERSION_LINE=$(grep -E "^pragma solidity" "$SOL_FILE" | head -n 1)
            if echo "$VERSION_LINE" | grep -qE "^pragma solidity [^;]+;"; then
                VERSION=$(echo "$VERSION_LINE" | sed -E 's/^pragma solidity[^0-9]*([0-9]+\.[0-9]+\.[0-9]+).*/\1/')
                SOLIDITY_VERSIONS+=("$VERSION")
            fi
        fi
    done

    # Remove duplicates from SOLIDITY_VERSIONS
    UNIQUE_VERSIONS=($(echo "${SOLIDITY_VERSIONS[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

    # Update hardhat.config.js with the extracted versions
    if [ ${#UNIQUE_VERSIONS[@]} -gt 0 ]; then
        echo "Adding Solidity versions to hardhat.config.js in $DIR..."
        COMPILERS_STRING=$(printf '{ version: "%s" },\n            ' "${UNIQUE_VERSIONS[@]}")
        COMPILERS_STRING=${COMPILERS_STRING%, } # Remove trailing comma

        HARDHAT_CONFIG="require(\"@nomicfoundation/hardhat-toolbox\");

    /** @type import('hardhat/config').HardhatUserConfig */
    module.exports = {
        solidity: {
            compilers: [
                $COMPILERS_STRING
            ]
        }
    };"

        echo "$HARDHAT_CONFIG" > hardhat.config.js
    else
        echo "No Solidity versions found in .sol files in $DIR."
    fi

    # Compile the smart contracts
    echo "Compiling contracts in $DIR..."
    npx hardhat compile || echo "Compilation failed in $DIR."

    # Return to the parent directory
    cd "$PARENT_DIR" || exit 1
}

export -f process_directory  # Export function to be used with xargs

# Find directories and process them concurrently
find "$PARENT_DIR" -mindepth 1 -maxdepth 1 -type d | xargs -P 8 -I {} bash -c 'process_directory "{}"'

echo "Script completed."
