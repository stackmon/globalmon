#!/bin/bash

# Parse command-line arguments
CONFIG_FILE="/usr/app/globalmon/config.yaml"  # Default config file
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --config)
        CONFIG_FILE="$2"
        shift
        shift
        ;;
        *)
        shift
        ;;
    esac
done

# Run my_app.py with the specified config file
globalmon --config "$CONFIG_FILE"  >> /var/log/globalmon/globalmon.log 2>&1
