#!/bin/bash

# Check if the given apache2 process is active
if ! pgrep apache2 > /dev/null; then
    # Start the apache2 process
    sudo service apache2 start

    # Log the taken action to a file
    date >> /var/log/apache2_start_log.txt
    echo "Apache2 started." >> /var/log/apache2_start_log.txt
else
    echo "Apache2 is already running."
fi