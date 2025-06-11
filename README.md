# File Encryption/Decryption Tool

A simple GUI-based Python application to encrypt and decrypt files using a password.

## Features
- Secure encryption using AES (via Fernet)
- Simple tkinter interface
- Password-based key generation

## How to Run
1. Install Python and dependencies:
pip install -r requirements.txt

2. Run the app:
python main.py

## Note
Encrypted files have `.encrypted` extension.
Decrypted files have `.decrypted` extension.
Use the same password to decrypt what you encrypted.
Do not lose the password – there's no recovery if it's lost.
Works with any file type.

**Test Cases:**
Try encrypting a .txt file
Then decrypt using the correct password
Try decrypting with a wrong password (should raise an error)

**5. How to Use the Tool**
      -A window will open.
      -Click Browse File to select any file (e.g., .txt, .pdf, etc.)
      -Enter a password/key.
      -Click Encrypt to encrypt the file.
           ~A new file like example.txt.encrypted will be created.
      -To decrypt:
           ~Select the .encrypted file
           ~Enter the same password
           ~Click Decrypt
           ~A file like example.txt.decrypted will appear.
