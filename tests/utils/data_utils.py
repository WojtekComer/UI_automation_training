import os

from cryptography.fernet import Fernet
from datetime import datetime


class DataUtils:

    @staticmethod
    def decrypt_secret(secret):
        key = os.getenv('SECRET_KEY')
        fernet_obj = Fernet(key)
        return fernet_obj.decrypt(secret).decode()

    @staticmethod
    def current_date_and_time():
        return datetime.now().strftime('%d-%m-%Y %H:%M:%S')
