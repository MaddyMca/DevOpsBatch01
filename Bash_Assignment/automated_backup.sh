#!/bin/bash

# Check if the shared directory exists
if [[ ! -d "/home/user/backup" ]]; then
    mkdir -p "/home/user/backup"
fi

# Compress the directory and its contents into a tarfile
tar -czvf "/home/user/backup/documents_backup.tar.gz" "/home/user/documents"

# Check the compression operation
if [[ $? -eq 0 ]]; then
    echo "Documents backup created successfully."
else
    echo "An error occurred while creating the backup."
fi