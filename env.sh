#!/bin/bash
# Parameters: log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
echo "Please enter the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL):"
read -r input_log_level

# Create .env file if it doesn't exist
if [ ! -e .env ]; then
    echo "Creating .env file..."
    touch .env
fi

if [ -z "$input_log_level" ]; then
    echo "No log level provided. Using default: INFO"
    LOG_LEVEL="INFO"
else
    LOG_LEVEL=$(echo "$input_log_level" | tr '[:lower:]' '[:upper:]')
fi

# Set the log level in the .env file
if grep -q "^LOG_LEVEL=" ./.env; then
    sed -i "s#^LOG_LEVEL=.*#LOG_LEVEL=$LOG_LEVEL#" ./.env
else
    echo "LOG_LEVEL=$LOG_LEVEL" >> ./.env
fi