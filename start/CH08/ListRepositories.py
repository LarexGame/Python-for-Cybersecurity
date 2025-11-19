#!/usr/bin/env python3
# Script that lists repositories in GitHub
# Requires a Personal Access Token to run
# By Garcia 11/17

import os
import configparser

# Funtionto get API Key
def get_api_key(key_name):
    # get location of secret file
    home_dir = os.path.expanduser('~')
    secrets_file = os.path.join(home_dir, "secrets.ini")
    # Create configparser object, load file
    config = configparser.ConfigParser()
    config.read(secrets_file)
    # Get key and return
    api_key = config["APIKeys"][key_name]
    return api_key

# Get key and print
token = get_api_key("github")
print(token)