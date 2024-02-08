# defines Account Class
# import random
# import string
from datetime import datetime


class Account:
    __website_name = ""
    __login_url = ""
    __username = ""
    __password = ""
    __last_changed = ""
    __map = {}

    def __init__(self, web_name, login_url, username, password, last_changed):
        self.__website_name = web_name
        self.__login_url = login_url
        self.__username = username
        self.__password = password
        self.__last_changed = last_changed
        Account.__map[login_url.lower()] = self  # Add account to the map

    def get_url(self):
        return self.__login_url

    def change_password(self, new_password):
        self.password = new_password
        self.__last_changed = str(datetime.now())

    def __str__(self):
        return (f"Website: {self.__website_name}\nURL: "
                f"{self.__login_url}\nUsername: {self.__username}"
                f"\nPassword: {self.__password}\nLast Password Change:"
                f" {self.__last_changed}")

    @classmethod
    def search(cls, url):
        return cls.__map[url.lower()]
