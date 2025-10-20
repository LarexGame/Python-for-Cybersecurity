#!/usr/bin/env python3
# ASCII generator
# Uses chr() to create ASCII characters
# By Garcia 10/20

# Create a loop 0 - 127

for num in range(128):
    # Print Value and chr() output
    print(f"{num} '{chr(num)}'")


