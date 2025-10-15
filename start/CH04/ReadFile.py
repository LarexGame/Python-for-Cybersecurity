#!/usr/bin/env python3
# Sample script that reads from a file
# By 

import os

# Get current director

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Build File Path

file_path = os.path.join(script_dir, "testfile.txt")

# Create File Object

f = open(file_path, "r")

# Read to file object

print(f.read())

# Close file Object

f.close()
