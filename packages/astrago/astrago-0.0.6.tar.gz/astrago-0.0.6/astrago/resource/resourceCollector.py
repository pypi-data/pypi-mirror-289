import os
import psutil

from astrago.resource.resourceDTO import Resource


def monitor_system_resources() -> Resource:
    pid = os.getpid()
    py = psutil.Process(pid)

    cpu_usage = os.popen("ps aux | grep " + str(pid) + " | grep -v grep | awk '{print $3}'").read()
    cpu_usage = cpu_usage.replace("\n", "")

    memory_usage = round(py.memory_info()[0] / 2. ** 30, 2)
    return Resource(cpu_usage, memory_usage, '0', '0')
