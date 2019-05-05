#!/usr/bin/env python3
# pw.py -inscerure password locker
import pyperclip, time, json, os, base64
from getpass import getpass
file = "pass.txt"
filepath = os.path.abspath("pass.txt")


def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


if os.path.isfile(filepath):
    open(file, "r+")
    if is_non_zero_file(filepath):
        passwords = json.load(open(file))
    else:
        passwords = {}
else:
    open(file, "w")
    passwords = {}
    print("This ")


def menu():
    print("----------------------")
    print("Password Locker")
    print("----------------------")
    print("1. Find Password")
    print("2. Save Password")
    print("3. Exit")
    print("----------------------")

    option = int(input("Enter option:"))

    while option:
        if option == 1:
            findPassword()
        elif option == 2:
            savePassword()
        elif option == 3:
            break
        else:
            print("Invalid option")
        print("------------------")
        option = int(input("Enter option:"))


def savePassword():
    account = input("Enter website/email:\n")
    print("Enter password")
    password = getpass()
    decoded_password = base64.encodestring(password.encode())
    passwords[account] = decoded_password.decode('ascii')
    json.dump(passwords, open(file, "w"))
    print("Password Saved")


def findPassword():
    account = input("Enter website/email:\n")
    if account in passwords.keys():
        encrypted_pass = base64.b64decode(passwords[account])
        pass_decode = encrypted_pass.decode('ascii')
        pyperclip.copy(pass_decode)
        print("Password copied for 10 seconds")
        time.sleep(10)
        pyperclip.copy("")
        print("Password destroyed")
    else:
        print("Account not found")


menu()
