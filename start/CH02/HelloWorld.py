#!/usr/bin/env python3
# A simple "Hello World" script in python
# Created by Rene Garcia 9/29

#ask user for a name
name = input("What is your name?")

# print hello to the user

print ("Hello " + name)
print ("Hello {0}".format(name))
print ("Hello", name)
print (f'Hello {name}')

message = "Hello " + name
print (message)

