#!/bin/bash

# Validate if a file name was provided as an argument
if [[ $# -eq 0 ]]; then
    echo "Please provide a file to check the permissions."
    exit 1
fi

# read the file name from the argument
file=$1

# Check if the file exists
if [[ ! -f "$file" ]]; then
    echo "The file $file does not exist."
    exit 1
fi

# Check the file for read permission
if [[ -r "$file" ]]; then
    echo "The file $file has read permission."
else
    echo "The file $file does not have read permission."
fi

# Check the file for write permission
if [[ -w "$file" ]]; then
    echo "The file $file has write permission."
else
    echo "The file $file does not have write permission."
fi

# Check the file for execute permission
if [[ -x "$file" ]]; then
    echo "The file $file has execute permission."
else
    echo "The file $file does not have execute permission."
fi