#!/bin/bash

# Log file name (replace with your name)
LOG_FILE="cs1500advices/Drew.Trigg.advices"

# Get current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Fetch advice from API
ADVICE=$(curl -s https://api.adviceslip.com/advice | jq -r '.slip.advice')

# Append advice with timestamp to log file
echo "[$TIMESTAMP] $ADVICE" >> "$LOG_FILE"

