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
            uri = "mongodb+srv://jay_dev:Mooey2022_morning@jaydev.t6afjfu.mongodb.net/?retryWrites=true&w=majority"
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
    def read_lists(cls):
        cls.connect()
        lists = list(cls.__account_list_collection.find())
        print(lists)

    @classmethod
    def rebuild_data(cls):
        cls.connect()
        all_accounts, all_lists = cls.read_data()
        list_dicts = [list.to_dict() for list in all_lists]
        for list in all_lists:
            print(list)
        cls.__account_list_collection.insert_many(list_dicts)
    @staticmethod
    def read_data():
        gmail = Account(web_name="Gmail", login_url="https://www.gmail.com", username="Jaywashere", password="123", last_changed=str(datetime.now()))

        pcc = TwoFactorAuth(name="Portland Community College", url="https://www.pcc.edu", username="kim.smith", password="321", _type="pin", _info="4444", last_changed=str(datetime.now()))

        school = AccountList(title="School", security_level="5", accounts=[pcc])
        personal = AccountList(title="Personal", security_level="7", accounts=[gmail])

        all_accounts = AccountList(title=AccountList.ALL_ACCOUNTS, security_level="10", accounts=[gmail, pcc])
        all_lists = [school, personal, all_accounts]

        return all_accounts, all_lists


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
    Database.rebuild_data()
    Database.read_lists()
