#!/usr/bin/env python3
# Script that scans web server logs for 404 errors
# By Garcia 11/03


import os

# Ask which file to open
log_file = input("Which file to Analyze? ")

# Get current director
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
# Build File Path
file_path = os.path.join(script_dir, log_file)

# Open log file
f = open(file_path, "r")

# Read the file line by line
while True:
    line = f.readline()
    if not line:
        break
    # Check for 404
    if "404" in line:
        if "administrator" in line:
            if "%" in line:
                # Print line
                print(line)            
        
# Close File
f.close()