from random import randint
from datetime import datetime
from uuid import uuid4
import sys
import os


def encrypt_key(key, shift):
    encrypted_key = [str((num + shift) % 10) for num in key]
    encrypted_key_str = ''.join(encrypted_key)
    return encrypted_key_str


def decrypt_key(encrypted_key_str, shift):
    encrypted_key = [int(char) for char in encrypted_key_str]
    decrypted_key = [(num - shift) % 10 for num in encrypted_key]
    return decrypted_key


def keygen():
    key_arr = []
    key_length = 10
    filename = 'secret_key'

    i = 0
    while i < key_length:
        rand = randint(1, 9)
        key_arr.append(rand)
        i = i + 1

    with open(filename, 'w') as f:
        f.write(encrypt_key(key_arr, 10))
        
    print(f"Secret key saved at {os.getcwd()}/{filename}")
    return key_arr


def hashman(password, hashkey):
    encrypted_pass = ""
    key_len = len(hashkey)
    for i in range(len(password)):
        shift = hashkey[i % key_len]
        encrypted_pass += chr(ord(password[i]) + shift)

    with open('encrypted_password', 'w') as f:
        f.write(encrypted_pass)
    
    print(f"Encrypted password saved at {os.getcwd()}/encrypted_password")
    
    return encrypted_pass


def unhashman(secret_key, encrypted_pass):
    decrypted_pass = ""
    key = [int(char) for char in secret_key]
    key_len = len(key)
    key_index = 0
    for char in encrypted_pass:
        shift = key[key_index]
        decrypted_pass += chr(ord(char) - shift)
        key_index = (key_index + 1) % key_len

    with open('decrypted_password', 'w') as f:
        f.write(decrypted_pass)
    
    print(f"Decrypted password saved at {os.getcwd()}/decrypted_password")
    
    return decrypted_pass

def title():
    title = """    ____              __          ______               
   / __ \____  __  __/ /_  ____ _/ ____/___  _________ 
  / / / / __ \/ / / / __ \/ __ `/ /   / __ \/ ___/ __ \\
 / /_/ / /_/ / /_/ / /_/ / /_/ / /___/ /_/ / /  / /_/ /
/_____/\____/\__,_/_.___/\__,_/\____/\____/_/  / .___/ 
                                              /_/      """
    print(title)


def prompt():
    while True:
        title()
        print(f"1. Encrypt password\n2. Decrypt password\n99. Exit")
        choise = int(input('> '))

        if choise == 1:
            os.system('clear')
            password = input('Password : ')
            hashman(password, keygen())
            input('press Enter')
        elif choise == 2:
            os.system('clear')
            hashed_pass = input('Crypted password : ')
            secret_key = input('Secret key : ')
            unhashman(secret_key, hashed_pass)
            input('press Enter')
        elif choise == 99:
            os.system('clear')
            print('bye.')
            exit(0)

        os.system('clear')

def main():
    prompt()

# Uncomment this line to try in the terminal.
# main()