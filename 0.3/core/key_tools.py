from cryptography.fernet import Fernet

def generate(use=".."):
    ask = input("Are you sure you want to generate a new key? [y/n]: ")
    if ask.lower() == "y":
        key = Fernet.generate_key()
        new_key_write = key.decode("utf-8")
        with open(f"{use}DATA/KEY", "w") as f:
            f.write(new_key_write)
    elif ask.lower() == "n":
        exit()
    else:
        print("Please enter either 'y'[Y] or 'n'[N]")