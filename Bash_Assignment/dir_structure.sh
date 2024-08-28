#!/bin/bash

# Create the main directory
mkdir -p /home/user

# Create sub-directories under the main directory
mkdir -p /home/user/projects 
mkdir -p /home/user/documents 
mkdir -p /home/user/downloads

# Create folder under the projects directory
mkdir -p /home/user/projects/project1
mkdir -p /home/user/projects/project2 
mkdir -p /home/user/projects/project3

# to check if all folders/sub-folders were created successfully
if [[ $? -eq 0 ]]; then
    echo "Folder structure created successfully."
else
    echo "An error occurred while creating structure."
fi