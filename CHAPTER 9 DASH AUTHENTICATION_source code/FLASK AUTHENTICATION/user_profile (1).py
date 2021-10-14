from cryptography.fernet import Fernet
import pandas as pd
import io
key = Fernet.generate_key()
fernet_key = Fernet(key)
password_file = r"C:\Users\i5 lenov\Desktop\zport\archive\password.bin"
with open(password_file, mode='rb') as file:
    password = file.read()
encrypted_token = fernet_key.encrypt(password)
decrypted_token = fernet_key.decrypt(encrypted_token)
user_password = decrypted_token.decode()
user_name_file = r"C:\Users\i5 lenov\Desktop\zport\archive\user__name.bin"
with open(user_name_file, mode='rb') as file:
    user_names = file.read()
def users_details():
    return user_password, user_names