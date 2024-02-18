from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Database:
    __client = None
    __accounts_collection = None
    __account_list_collection = None

    @classmethod
    def connect(cls):
        if cls.__client is None:
            uri = "mongodb+srv://jay_dev:<password>@jaydev.t6afjfu.mongodb.net/?retryWrites=true&w=majority"
            # Create a new client and connect to the server
            client = MongoClient(uri, server_api=ServerApi('1'))
            print(client)
            accounts_database = client.Accounts
            cls.__accounts_collection = accounts_database.Accounts
            cls.__account_list_collection = accounts_database.Account_lists
            print(accounts_database)
            print(cls.__accounts_collection)
            print(cls.__account_list_collection)

    @classmethod
    def rebuild_data(cls):
        



# Old method:
# def test_database():
#     print("Welcome to Pymongo!")
#     client = MongoClient("mongodb+srv://jay_dev:Mooey2022_morning@jaydev.t6afjfu.mongodb.net/?retryWrites=true&w=majority")
#     print(client)
#     db = client.PasswordAccounts
#     print(db)
#     accounts = db.Accounts
#     print(accounts)


if __name__ == '__main__':
    Database.connect()

