from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList
from datetime import datetime
from pymongo import *


class Database:
    @staticmethod
    def read_data():
        pass
    

def test_database():
    print("Welcome to Pymongo!")
    client = MongoClient("mongodb+srv://jay_dev:Mooey2022_morning@jaydev.t6afjfu.mongodb.net/?retryWrites=true&w=majority")
    print(client)


if __name__ == '__main__':
    test_database()
