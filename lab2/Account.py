# defines Account Class
import random
import string
from datetime import datetime


class Account:
    __name = __url = __username = password = ""
    __type = False
    __accounts = []
    __map = {}
    ALL_ACCOUNTS = "All Accounts"

    def __init__(self, name, url, username, password, _type):
        self.__name = name
        self.__url = url
        self.__username = username
        self.__type = _type
        self.__password = password if password else self.generate_password
        self.__last_password_change_date = datetime.now()

    def __str__(self):
        return f"<Category: {self.__name}>"

    def __iter__(self):
        return self.__accounts.__iter__()

    def get_name(self):
        return self.__name

    @staticmethod
    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(length))
        return new_password

    def change_password(self, new_password):
        self.__password = new_password
        self.__last_password_change_date = datetime.now()

    def __str__(self):
        return (f"Website: {self.__website_name}\nURL: "
                f"{self.__url}\nUsername: {self.__username}"
                f"\nPassword: {self.__password}\nLast Password Change:"
                f" {self.__last_password_change_date}")

    @classmethod
    def search(cls, url):
        return cls.__map[url.lower()]
