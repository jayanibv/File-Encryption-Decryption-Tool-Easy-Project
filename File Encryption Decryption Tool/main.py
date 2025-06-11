import os
from tkinter import Tk, Label, Button, filedialog, Entry, messagebox, StringVar
from cryptography.fernet import Fernet
import base64
import hashlib

# Generate a Fernet key from a password
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# Encrypt a file
def encrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        key = generate_key(password)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        encrypted_file_path = file_path + ".encrypted"
        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted)

        messagebox.showinfo("Success", f"File encrypted: {encrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Decrypt a file
def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        key = generate_key(password)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        decrypted_file_path = file_path.replace(".encrypted", ".decrypted")
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted)

        messagebox.showinfo("Success", f"File decrypted: {decrypted_file_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Browse and set file path
def browse_file():
    path = filedialog.askopenfilename()
    file_path_var.set(path)

# GUI setup
app = Tk()
app.title("File Encryption/Decryption Tool")
app.geometry("400x200")

file_path_var = StringVar()
file_path = Entry(app, textvariable=file_path_var, width=40)
file_path.pack(pady=10)

browse_button = Button(app, text="Browse File", command=browse_file)
browse_button.pack()

Label(app, text="Enter Password").pack()
password_entry = Entry(app, show='*', width=30)
password_entry.pack(pady=5)

Button(app, text="Encrypt", command=lambda: encrypt_file(file_path_var.get(), password_entry.get())).pack(pady=5)
Button(app, text="Decrypt", command=lambda: decrypt_file(file_path_var.get(), password_entry.get())).pack(pady=5)

app.mainloop()
