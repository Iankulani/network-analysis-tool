# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 05:54:47 2024

@author: IAN CARTER KULANI
"""

import socket
import psutil
import os

def get_open_ports(ip):
    open_ports = []
    for port in range(1, 65535):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
    return open_ports

def get_server_info(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
    except socket.herror:
        hostname = "Unknown"
   
    return {
        "IP Address": ip,
        "Hostname": hostname,
        "Open Ports": get_open_ports(ip)
    }

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_info():
    memory_info = psutil.virtual_memory()
    return {
        "Total Memory": memory_info.total,
        "Available Memory": memory_info.available,
        "Used Memory": memory_info.used,
        "Memory Percentage": memory_info.percent
    }

def main():
    print("=========================Welcome to the Cyber drill Penetration Tool=========================")
    ip = input("Enter the IP address to analyze: ")

    server_info = get_server_info(ip)
    cpu_usage = get_cpu_usage()
    memory_info = get_memory_info()

    print("\nServer Information:")
    print(f"IP Address: {server_info['IP Address']}")
    print(f"Hostname: {server_info['Hostname']}")
    print(f"Open Ports: {server_info['Open Ports']}")
   
    print("\nCPU Usage:")
    print(f"CPU Usage: {cpu_usage}%")
   
    print("\nMemory Information:")
    for key, value in memory_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()