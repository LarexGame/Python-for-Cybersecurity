#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Garcia 11/12

import hashlib
import requests

def SHA1(msg):
    return hashlib.sha1(msg.encode()).hexdigest()
def test_password(preffix):

    url = "https://api.pwnedpasswords.com/range/" + preffix
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # Save response to variable
    raw_text = response.text
    # Split on CRLF
    raw_list = raw_text.split("\r\n")
    # Separate on :, save to dictionary
    raw_dict = {}
    for item in raw_list:
        split_results = item.split(":")
        raw_dict[split_results[0]] = split_results[1]
    # Return dictionary
    return raw_dict

# Ask User for password
password = input("Password: ")

# Hash Password
pass_hash = SHA1(password)
pass_hash = pass_hash.upper()

# Split password
hash_preffix = pass_hash[0:5]
hash_suffix = pass_hash[5:]

# Call API
results = test_password(hash_preffix)

# Search Results
if hash_suffix in results.keys():
    print(f"Password is bad, it has been found {results[hash_suffix]} times")
else:
    print("Password is safe")