#!/bin/bash

# ensure there is an argumet with directory was provided.
if [[ $# -eq 0 ]]; then
    echo "Please provide a directory name as an argument."
    exit 1
fi

# Get the directory name as argument
directory=$1

# capturing the current date and time into the variable
timestamp=$(date +%Y-%m-%d_%H-%M-%S) 
# captture the name the backup directory with timestamp
backup_dir="backup_$timestamp"

# Create the backup directory
mkdir -p "$backup_dir"

# Copy all .txt files from the provided directory to the backup directory
cp "$directory"/*.txt "$backup_dir"

# Check if the copying was successful 
if [[ $? -eq 0 ]]; then
    echo "Backup created successfully in $backup_dir"
else
    echo "An error occurred while creating the backup or there are no text files in the provided dir"
fi