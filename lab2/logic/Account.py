# defines Account Class
import random
import string
from datetime import datetime


class Account:
    __map = []

    def __init__(self, web_name, login_url, username, password, last_password_change_date=None):
        self.web_name = web_name
        self.login_url = login_url
        self.username = username
        self.password = password
        self.last_password_change_date = last_password_change_date if last_password_change_date else datetime.now()
        self.__map[login_url.lower()] = self  # Add account to the map

    # @staticmethod
    # def generate_password(self, length=12):
    #     characters = string.ascii_letters + string.digits + string.punctuation
    #     new_password = ''.join(random.choice(characters) for _ in range(length))
    #     return new_password

    def change_password(self, new_password):
        self.password = new_password
        self.last_password_change_date = str(datetime.now())

    def __str__(self):
        return (f"Website: {self.web_name}\nURL: "
                f"{self.login_url}\nUsername: {self.username}"
                f"\nPassword: {self.password}\nLast Password Change:"
                f" {self.last_password_change_date}")

    @classmethod
    def search(cls, url):
        return cls.__map[url.lower()]
