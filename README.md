# 🚨 **KillOS + Desktop Ransomware** 🚨

Welcome to **KillOS + Desktop Ransomware**, a project created for educational and demonstration purposes, showcasing the devastating effects of ransomware on a Linux/Unix-based system. This repository is designed to help students and cybersecurity enthusiasts understand how ransomware and malware operate. ⚠️ **Use Responsibly** ⚠️

## ⚡ How it Works

### 🖥️ **Desktop Ransomware**
This part of the demo contains the `ransomware.py` script, which when executed on a Linux or Unix system:
- 🛑 **Encrypts** the entire `Desktop` directory.
- 📝 **Displays a ransom note** to the user, instructing them to pay a ransom for decryption.

To decrypt files:
1. Run the `decrypt.py` script.
2. It will ask for a **passkey**. This passkey is provided by the "hacker" after ransom is paid (in real scenarios).
3. If the correct passkey is entered, the files will be **decrypted** and restored.

### 💀 **KillOS**
The `killos` directory contains a dangerous script that, when executed:
- 🔥 **Encrypts the boot directory**, rendering the system **unbootable**.
- This script requires **root privileges** to function, making the entire system unrecoverable unless proper backups are in place.

### ⚠️ **Warning**
- **DO NOT** run this script on any system that contains important data or has not been backed up.
- This script is for **educational purposes only** and should be used in a controlled environment like virtual machines.

## ⚙️ **Usage**

### 🖥️ **Desktop Ransomware**
1. Clone the repository:
   ```bash
   git clone https://github.com/YourRepo.git
   ```
2. Navigate to the `ransomware` directory:
   ```bash
   cd ransomware
   ```
3. Execute the ransomware:
   ```bash
   python3 ransomware.py
   ```
4. To decrypt:
   ```bash
   python3 decrypt.py
   ```

### 💀 **KillOS**
1. Navigate to the `killos` directory:
   ```bash
   cd killos
   ```
2. Execute the script with root privileges (⚠️ *Dangerous!*):
   ```bash
   sudo python3 killos.py
   ```

## 🎓 **Disclaimer**

This project is designed for **educational purposes only** to demonstrate how ransomware works. **Do not** use this on any unauthorized systems. The creator takes no responsibility for any misuse of this project.

---

Built by **Vansh Thakkar** 🛠️

---
