# Solution for backing up files

import psutil
import time

try:

    while True:
        cpu_usage = psutil.cpu_percent()
        print (cpu_usage)
        if cpu_usage > 80:
            print ("CPU Usage Alert, its usage is above thershold", cpu_usage)
            time.sleep(5)
    print ("CPU Usgae is within the threshold" , cpu_usage)
    time.sleep(5)
except KeyboardInterrupt:
    print("Program interrupted by user")
