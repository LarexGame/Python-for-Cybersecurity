#!/usr/bin/env python3
# Sample script that writes to a file
# By Garcia 10/15




import os

# Get current director

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

# Build File Path

file_path = os.path.join(script_dir, "testfile.txt")

# Create File Object

f = open(file_path, "w")

# Write to file object

f.write("My Name is Alex\n")
f.write("I like rubber ducks\n")
f.write("Hello World\n")

# Close file Object

f.close()
