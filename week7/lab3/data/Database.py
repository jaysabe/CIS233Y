from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList
from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Database:
    __client = None
    __accounts_database = None
    __accounts_collection = None
    __account_list_collection = None

    @classmethod
    def connect(cls):
        if cls.__client is None:
            uri = "mongodb+srv://jay_dev:Mooey2022_morning@jaydev.t6afjfu.mongodb.net/?retryWrites=true&w=majority"
            # Create a new client and connect to the server
            cls.__client = MongoClient(uri, server_api=ServerApi('1'))
            print(cls.__client)
            cls.__accounts_database = cls.__client.PasswordManager
            cls.__accounts_collection = cls.__accounts_database.Accounts
            cls.__account_list_collection = cls.__accounts_database.AccountLists
            # print(cls.__accounts_database)
            # print(cls.__accounts_collection)
            # print(cls.__account_list_collection)

    @classmethod
    def read_lists(cls):
        cls.connect()
        list_dicts = list(cls.__account_list_collection.find())
        print(list(cls.__account_list_collection.find()))
        # for a_list in list_dicts:
        #     print(a_list)
        list_objects = [AccountList.build(list_dict) for list_dict in list_dicts]

        return AccountList.lookup(AccountList.ALL_ACCOUNTS.lower()), list_objects

    @classmethod
    def read_accounts(cls):
        cls.connect()
        account_dicts = list(cls.__accounts_collection.find())

        account_objects = [Account.build(account_dict) for account_dict in account_dicts]

    @classmethod
    def rebuild_data(cls):
        cls.connect()
        cls.__account_list_collection.drop()
        cls.__account_list_collection = cls.__accounts_database.AccountLists
        cls.__accounts_collection.drop()
        cls.__accounts_collection = cls.__accounts_database.Accounts
        all_accounts, all_lists = cls.build_test_data()
        list_dicts = [list.to_dict() for list in all_lists]
        # for list in all_lists:
        #     print(list)
        cls.__account_list_collection.insert_many(list_dicts)

        account_dicts = [account.to_dict() for account in all_accounts]
        cls.__accounts_collection.insert_many(account_dicts)

    @classmethod
    def read_data(cls):
        cls.read_accounts()
        all_accounts_list, list_of_all_lists = cls.read_lists()
        return all_accounts_list, list_of_all_lists

    @staticmethod
    def build_test_data():
        gmail = Account(name="Gmail", url="https://www.gmail.com", username="Jaywashere", password="123", last_changed=str(datetime.now()))
        bing = Account(name="Bing", url="bing.com", username="jordmar12", password="pegeseus45", last_changed=str(datetime.now()))
        iqcu = TwoFactorAuth(name="IQ Credit Union", url="https://www.iqcu.com", username="mark.camele", password="bestyear2022", type="pin", info="4077", last_changed=str(datetime.now()))
        pcc = TwoFactorAuth(name="Portland Community College", url="https://www.pcc.edu", username="kim.smith", password="321", type="pin", info="4444", last_changed=str(datetime.now()))

        school = AccountList(title="School", security_level=5, accounts=[pcc])
        personal = AccountList(title="Personal", security_level=7, accounts=[gmail, iqcu, bing])
        finance = AccountList(title="Finance", security_level=10, accounts=[iqcu])

        all_accounts = AccountList(title=AccountList.ALL_ACCOUNTS, security_level=10, accounts=[gmail, bing, iqcu, pcc])
        all_lists = [school, personal, finance, all_accounts]

        return all_accounts, all_lists

    @classmethod
    def add_list(cls, a_list):
        cls.connect()
        cls.__account_list_collection.update_one({"_id": a_list.get_key()}, {"$set": a_list.to_dict()}, upsert=True)

    @classmethod
    def add_account(cls, acc):
        cls.connect()
        cls.__accounts_collection.update_one({"_id": acc.get_key()}, {"$set": acc.to_dict()}, upsert=True)

    @classmethod
    def delete_list(cls, a_list):
        cls.connect()
        cls.__account_list_collection.delete_one({"_id": a_list.get_key()})


if __name__ == '__main__':
    Database.rebuild_data()
    Database.read_accounts()
    Database.read_lists()
