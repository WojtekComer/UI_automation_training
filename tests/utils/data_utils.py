import os

from cryptography.fernet import Fernet


class DataUtils:

    @staticmethod
    def decrypt_secret(secret):
        key = os.getenv('SECRET_KEY')
        fernet_obj = Fernet(key)
        return fernet_obj.decrypt(secret).decode()
