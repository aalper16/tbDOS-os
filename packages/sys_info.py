import platform
import os 
import psutil

def get_os():
     return platform.system()

def get_version():
    return platform.version()

def get_type():
    return platform.architecture()[0]

def get_processor():
    return platform.processor()

def get_python():
    return platform.python_version()

def get_ram():
    ram_info = psutil.virtual_memory()
    total_ram_mb = ram_info.total / (1024 ** 2)
    return str(total_ram_mb)