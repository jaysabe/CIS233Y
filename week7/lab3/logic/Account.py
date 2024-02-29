# defines Account Class
# import random
# import string
from datetime import datetime


class Account:
    __name = ""
    __url = ""
    __username = ""
    __password = ""
    __last_changed = ""
    __map = {}

    def __init__(self, name, url, username, password, last_changed):
        self.__name = name
        self.__url = url
        self.__username = username
        self.__password = password
        self.__last_changed = last_changed
        Account.__map[self.get_key()] = self  # Add account to the map


    @classmethod
    def build(cls, dict):
        from logic.TwoFactorAccount import TwoFactorAuth

        if dict["authentication"] == "Regular":
            return Account(dict["name"], dict["url"], dict["username"], dict["password"], dict["last_changed"])
        elif dict["authentication"] == "TwoFactorAccount":
            return TwoFactorAuth(dict["name"], dict["url"], dict["username"], dict["password"], dict["type"],
                                 dict["value"], dict["last_changed"])

        else:
            raise Exception(f"Unknown site type: {dict['type']}!")

    def get_key(self):
        return f"{self.__name}: {self.__username}".lower()

    def get_name(self):
        return self.__name

    def get_username(self):
        return self.__username

    def change_password(self, new_password):
        self.__password = new_password
        self.__last_changed = str(datetime.now())

    def __str__(self):
        return (f"Website: {self.__name}\nURL: "
                f"{self.__url}\nUsername: {self.__username}"
                f"\nPassword: {self.__password}\nLast Password Change:"
                f" {self.__last_changed}")

    @classmethod
    def search(cls, key):
        return cls.__map[key.lower()]

    def to_dict(self):
        return {
            "_id": self.get_key(),
            "authentication": "Regular",
            "name": self.__name,
            "url": self.__url,
            "username": self.__username,
            "password": self.__password,
            "last_changed": self.__last_changed,
        }

    def add_to_database(self):
        from data.Database import Database

        Database.add_account(self)
