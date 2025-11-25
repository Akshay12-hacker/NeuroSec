import psutil, datetime

def system_status():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return {
        "cpu_usage": f"{cpu}%",
        "memory_usage": f"{memory}%",
        "system_boot_time": boot_time
    }

