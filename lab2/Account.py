# defines Account Class
import random
import string
from datetime import datetime


class Account:
    def __init__(self, website_name=None, url=None, username=None, _type=None, password=None):
        self._website_name = website_name
        self._url = url
        self._username = username
        self._type = _type
        self._password = password if password else self.generate_password
        self._last_password_change_date = datetime.now()

    @staticmethod
    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(length))
        return new_password

    def change_password(self, new_password):
        self._password = new_password
        self._last_password_change_date = datetime.now()

    def __str__(self):
        return (f"Website: {self._website_name}\nURL: "
                f"{self._url}\nUsername: {self._username}"
                f"\nPassword: {self._password}\nLast Password Change:"
                f" {self._last_password_change_date}")
