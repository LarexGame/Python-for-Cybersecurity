#!/usr/bin/env python3
# First example of pinging from Python
# By Rene Garcia 10/08

#Import things
import os 

#Assign IP to a Variable
ip_addr = "127.0.0.1"

#Build ping command
ping_cmd = "ping -c 1 -w 2 " + ip_addr + "> /dev/null 2>&1"

#Execute ping command
exit_code = os.system(ping_cmd)

#Print results
print(exit_code)
if exit_code == 0:
    print(f"{ip_addr} is online")
else:
    print(f"{ip_addr} is NOT online")