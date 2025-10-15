#!/usr/bin/env python3
# First example of pinging from Python
# By Rene Garcia 10/08

#Import things
import os 
import platform

def ping_address(ip_address):
    #Find Current OS
    current_os = platform.system().lower()

    # If Windows
    if current_os == "Windows":
        ping_cmd = "ping -n 1 -w 2 " + ip_address + " > nul" 
    else:
        ping_cmd = "ping -c 1 -w 2 " + ip_address + "> /dev/null 2>&1"

    #Execute ping command
    exit_code = os.system(ping_cmd)
    return exit_code

#Assign IP to a Variable
ip_prefix = "192.168.0."

# Start a Loop
for final_octet in range(254):

    #Build IP Address
    ip_addr = ip_prefix + str(final_octet + 1)

    exit_code = ping_address(ip_addr )

    #Print results
    #print(exit_code)
    if exit_code == 0:
        print(f"{ip_addr} is online")
    else:
        print(f"{ip_addr} is NOT online")