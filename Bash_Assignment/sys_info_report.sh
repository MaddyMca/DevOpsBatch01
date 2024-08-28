#!/bin/bash

# Get system uptime
uptime > system_report.txt

# Get memory usage
free -h >> system_report.txt

# Get CPU load %
top -bn1 | grep "Cpu(s)" | awk '{print $2}' >> system_report.txt

# Get disk usage
df -h >> system_report.txt

# Get running processes
ps aux >> system_report.txt