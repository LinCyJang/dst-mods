import platform
import os
import socket
import psutil

def get_system():
    system = platform.system()
    version = platform.version()
    # dist = platform.dist()
    system_info = {
      'system': system,
      'version': version,
      # 'dist': dist
    }
    
    return system_info

def get_dir():
    cwd = os.getcwd()
    
    return cwd
  
def get_newwork():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    
    network_info = {
      "host": host,
      "ip": ip
    }
    return network_info

def get_cpu():
  cpu = psutil.cpu_count()
  cpu_percent = psutil.cpu_percent(interval=None, percpu=False)
  memory = psutil.virtual_memory()
  
  cpu_info = {
    "cpu": cpu,
    "memory": memory,
    "cpu_percent": cpu_percent
  }
  
  return cpu_info