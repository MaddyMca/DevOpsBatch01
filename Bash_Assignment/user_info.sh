#!/bin/bash

# Get logged in user information from the env variables on the shell
u_name=$(whoami)
uid=$(id -u)
gid=$(id -g)
home_dir=$(getent passwd "$username" | cut -d: -f7)
shell_used=$(getent passwd "$username" | cut -d: -f8)

# Display the information
echo "Username: $u_name"
echo "User ID: $uid"
echo "Group ID: $gid"
echo "Home Directory: $home_dir"
echo "Shell: $shell_used"