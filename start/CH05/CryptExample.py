#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Garcia 10/22


from cryptography.fernet import Fernet
# Create Funtion
# Fernet create key
def fernet_create_key():
    key = Fernet.generate_key()
    return key

# Fernet Encrypt
def fernet_encrypt(key, plain_text):
    key_b = key.encode()
    plain_text_b = plain_text.encode()
    cipher_text_b = Fernet (key_b).encrypt(plain_text_b)
    return cipher_text_b

# Fernet Decrypt
def fernet_decrypt(key, cipher_text):
    key_b = key.encode()
    cipher_text_b = cipher_text.encode()
    plain_text_b = Fernet(key_b).decrypt(cipher_text_b)
    return plain_text_b

# Ask what to do
print("*" * 80)
print("Welcome to Fernet encryption")
print("This script can create keys, encrypt, or decrypt")
task = input("What would you like to do? (c/e/d) ")[0].lower()


# If Encrypt
if task == "e":
    # Get Key and Data
    enc_key = input("What is the key: ")
    plain_text = input("What is the message: ")
    # Call Encrpyt funtion 
    cipher_text_b = fernet_encrypt(enc_key, plain_text)
    # Print out results
    print("Your encrypted message is")
    print(f"'{cipher_text_b.decode()}'")

# If Decrypt
elif task == "d":
    # Get Key and Data
    enc_key = input("What is the key: ")
    cipher_text = input("What is the encrypted message: ")
    # Call Decrypt funtion 
    cipher_text_b = fernet_decrypt(enc_key, cipher_text)
    # Print out results
    print("Your Decrypted message is")
    print(f"'{cipher_text_b.decode()}'") 

# If Create key
elif task == "c":
    # Call Create funtion
    enc_key_b = fernet_create_key()
    # Print out results
    enc_key = enc_key_b.decode()
    print(f"Encrpytion key '{enc_key}'")

else:
    print("Please answer c/e/d")

# Key -- INrLLvZtyBwEAfNvxNnhAfMMgM_oKqLVokuyUOKoF8w= --
# Encrpyted message -- AAAAABo-Qo6J9pYqSfm8SPrQkKIZ40UfS_HlhwTC7hbAAORT_q-gVs4R7edhgrS5cXGFlubjyRT46qxDxxzRQyFWB8IN_67FQ==