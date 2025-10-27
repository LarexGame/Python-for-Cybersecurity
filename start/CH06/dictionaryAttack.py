#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Garcia 10/27

import os
import sys
from passlib.hash import sha512_crypt

# Funtions
# Hash the guess
def hash_password(hash_type, salt, password):
    hash_salt = f"${hash_type}${salt}"
    my_hash = sha512_crypt.using(rounds=5000).hash(password, salt=hash_salt)
    return my_hash

# Load Dicctionary File
def read_dictionary(file_name):

    # Get current director
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)

    # Build File Path
    file_path = os.path.join(script_dir, file_name)

    # Create File Object
    f = open(file_path, "r")

    # Read to file object
    dictionary_file = f.read()

    # Close file Object
    f.close()
    return dictionary_file

# Get Hash string
password_hash = input("What is the password hash: ")

# Slipt hash
hash_parts = password_hash.split("$")
hash_type = hash_parts[1]
salt = hash_parts[2]

# Load Dictionary file
dictionary_list = read_dictionary("top10.txt")

# For each line in dictionary
for guess in dictionary_list:
    guess = guess.strip()
    # hash the guess
    guess_hash = hash_password(hash_type, salt, guess)
    # Is it a match
    if guess_hash == password_hash:
        # Print guess and quit
        print(f"Password Found: {guess}")
        # How to quit the Script?
        sys.exit(0)

print("Password not found")


#######################################
########## POSIBBLE FIXING ############
#######################################

import os
import sys
from passlib.hash import sha512_crypt

# Functions
def hash_password(salt, password):
    return sha512_crypt.using(salt=salt, rounds=5000).hash(password)

def read_dictionary(file_name):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, "r") as f:
        return f.readlines()

# Get Hash string
password_hash = input("What is the password hash: ")

# Split hash
hash_parts = password_hash.split("$")
hash_type = hash_parts[1]
salt = hash_parts[2]

# Load Dictionary file
dictionary_list = read_dictionary("top10.txt")

# Try each guess
for guess in dictionary_list:
    guess = guess.strip()
    guess_hash = hash_password(salt, guess)
    if guess_hash == password_hash:
        print(f"Password Found: {guess}")
        sys.exit(0)

print("Password not found")