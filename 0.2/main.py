"""
Made by OC17
WipeOut V0.2
2026/02/17
"""
# Import lists
import pwinput
from cryptography.fernet import Fernet
import os
import core.VAR as VAR
import random
import shutil
import time
import subprocess
import pathlib

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

        elif query in ["help", "-h"]:
            print(f"{VAR.help_me()}\n")

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

        elif query in ["makefile", "touch"]:
            file_name = input("File name: ")
            content = input("Content (can be edited later with rewrite or edit): ")
            with open(f"DATA\\sys\\{file_name}", "w") as new:
                new_content = bytes(content, "utf-8")
                encoded = key.encrypt(new_content)
                decoded = encoded.decode("utf-8")
                new.write(decoded)

        elif query in ["read", "me"]:
            file = input("File name: ")
            with open(f"DATA\\sys\\{file}", "r") as new:
                content = new.read()
                decrypt = key.decrypt(content)
            print(decrypt.decode("utf-8"))

        elif query in ["edit", "notepad"]:
            file = input("File name: ")
            temp = ""
            for i in range(3):
                temp_num = random.choice(VAR.num)
                temp+=temp_num
            with open(f"DATA\\sys\\{file}", "r") as new:
                content=new.read()
                new_decrypted_content = key.decrypt(content)
                new_decrypted_content = new_decrypted_content.decode("utf-8")
            with open(f"DATA\\sys\\{temp}{file}", "w") as new_temp:
                new_temp.write(new_decrypted_content)
            print("Waiting 3 seconds to assure file creation")
            time.sleep(3)
            subprocess.call(f"core\\nano.exe DATA\\sys\\{temp}{file}")
            with open(f"DATA\\sys\\{temp}{file}", "r") as new:
                content=new.read()
            with open(f"DATA\\sys\\{file}", "w") as new:
                new_content = bytes(content, "utf-8")
                encoded = key.encrypt(new_content)
                decoded = encoded.decode("utf-8")
                new.write(decoded)
            os.remove(f"DATA\\sys\\{temp}{file}")
        elif query in ["del", "rem"]:
            print(">WARNING<\nThis will remove the input file name")
            file = input("File name: ")
            os.remove(f"DATA\\sys\\{file}")
            print("File removed")

        elif query in ["tree", "get"]:
            print(VAR.get_tree())

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