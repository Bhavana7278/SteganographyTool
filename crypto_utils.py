from cryptography.fernet import Fernet
import base64
import hashlib

# ✅ Generate key from password
def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

# ✅ Encrypt message
def encrypt_message(message, password):
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

# ✅ Decrypt message
def decrypt_message(encrypted_message, password):
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()
