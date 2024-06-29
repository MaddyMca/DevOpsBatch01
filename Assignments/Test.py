import psutil

print("psutil.cpu_percent(interval=2) = %s" % (psutil.cpu_percent(interval=2),))

print("psutil.cpu_percent(interval=2) = %s" % (psutil.cpu_percent(interval=2),))

print("The number of CPUs is : %s" % (psutil.cpu_count(), ))

print("The CPU utilization of all the CPUs is: %s" % (psutil.cpu_percent(interval=2, percpu=True), ))