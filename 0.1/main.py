"""
Made by OC17
WipeOut V0.1
2026/02/09
"""
# Import lists
import pwinput
from cryptography.fernet import Fernet
import os
import core.VAR as VAR
import random
import shutil
import time

# Variables
with open("DATA/user.enc", "r") as f:
    user = f.read()
with open("DATA/password.enc", "r") as f:
    password = f.read()
with open("DATA/KEY", "r") as f:
    key = f.read()
    key = Fernet(key)

def cmd():
    user_ = key.decrypt(user.encode()).decode()
    while True:
        query = input(f"wipeout@{user_}:~$ ")

        if query in ["reset", "clear", "cls"]:
            os.system("cls")
        elif query in ["quit", "exit", "bye"]:
            exit(random.choice(VAR.quotes))
        elif query in ["wipeoutSYS", "rm -rf sys"]:
            ask = input("Are you sure? [Y/else] ")
            if ask.lower() == "y":
                shutil.rmtree("DATA/sys")
                time.sleep(0.5)
                location = os.path.abspath(__file__)
                location = location[:-7]
                print(f"{location}\\DATA\\sys")
                os.mkdir(f"{location}\\DATA\\sys")
                print("Removed all contents of sys")

def login():
    password_ = key.decrypt(password.encode()).decode()
    user_ = key.decrypt(user.encode()).decode()
    user_q = input("Username: ")
    password_q = pwinput.pwinput("Password: ")
    if user_ != user_q:
        print("Invalid credentials")
        exit()
    if password_ != password_q:
        print("Invalid credentials")
        exit()
    print("Welcome to WipeOut")
    cmd()
def main():
    os.system("cls")
    if user == "=":
        new_user = input("Username: ")
        new_user = bytes(new_user, "utf-8")
        new_user_enc = key.encrypt(new_user)
        decoded = new_user_enc.decode("utf-8")
        with open("DATA/user.enc", "w") as i:
            i.write(decoded)
    if password == "=":
        new_password = pwinput.pwinput("Password: ")
        new_password = bytes(new_password, "utf-8")
        new_password_enc = key.encrypt(new_password)
        decoded = new_password_enc.decode("utf-8")
        with open("DATA/password.enc", "w") as i:
            i.write(decoded)
    else:
        print("Already existing info, logging in.")
        login()
if __name__ == "__main__":
    main()