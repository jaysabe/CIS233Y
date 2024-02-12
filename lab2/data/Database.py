from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList
from datetime import datetime


class Database:
    @staticmethod
    def read_data():
        gmail = Account(web_name="Gmail", login_url="https://www.gmail.com", username="Jaywashere", password="123", last_changed=str(datetime.now()))

        pcc = TwoFactorAuth(name="Portland Community College", url="https://www.pcc.edu", username="kim.smith", password="321", _type="pin", _info="4444", last_changed=str(datetime.now()))

        school = AccountList(title="School", security_level="5", accounts=[pcc])
        personal = AccountList(title="Personal", security_level="7", accounts=[gmail])

        all_accounts = AccountList(title=AccountList.ALL_ACCOUNTS, security_level="10", accounts=[gmail, pcc])
        all_lists = [school, personal, all_accounts]

        return all_accounts, all_lists
