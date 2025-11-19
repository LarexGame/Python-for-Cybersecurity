#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By Garcia 11-19

import os
import configparser
import hashlib
import requests
import sys
# Funtions
# Check reports
def vt_get_report(api_key, file_hash):
    url = "https://www.virustotal.com/api/v3/files/" + file_hash
    payload={}
    headers = {
        'Accept': 'aplication/json',
        'x-apikey': api_key
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        results = response.json()
        return results

# Upload files for scan
def vt_upload_file(api_key, file_hash):
    pass
# Check scan status
def vt_scan_status(api_key, file_hash):
    pass
# Get APIKey
def get_api_key(key_name):
    # get location of secret file
    home_dir = os.path.expanduser('~')
    secrets_file = os.path.join(home_dir, "secret.ini")
    # Create configparser object, load file
    config = configparser.ConfigParser()
    config.read(secrets_file)
    # Get key and return
    api_key = config["APIKeys"][key_name]
    return api_key

# Hash File
def hash_file(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        # Read the file in chunks of 8192 bytes
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

# Get file to scan
target_file = input("Wich file to scan? ")
# Get file hash
file_hash = hash_file(target_file)
print(file_hash)
# Get report
token = get_api_key("virustotal")
file_report = vt_get_report(token, file_hash)
print(file_report)

# If report
if file_report:
    # Print results and quit
    data = file_report["data"]
    attributes = data["attributes"]
    last_stats = attributes["last_analysis_stats"]
    print("-" * 80)
    print(f"\tmalicious: {last_stats['malicious']}")
    print(f"\tsuspicious: {last_stats['suspicious']}")
    print(f"\tundetected: {last_stats['undetected']}")

    sys.exit()
# Else
else:
    print("File not Scanned")
    # Upload file
    # wait 30 seconds
    # Check scan status
    # Print results and quit