#!/bin/bash

# Check disk usage of the root filesystem
df -h / | awk '{print $5}' | head -n 1 | cut -d'%' -f1 | read disk_usage

# check if the disk usage is above 80%
if [[ $disk_usage -ge 80 ]]; then
    # send the email
    recipient_email="kiran_40221@yahoo.co.in"
    subject="Root folder Disk Usage Alert"
    message="Root folder has crossed the threshold $disk_usage%. Take appropriate action."

    # send mail
    sendmail "$recipient_email" -s "$subject" <<< "$message"
fi