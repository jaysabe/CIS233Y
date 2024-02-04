# defines password manager
from input_validation import select_item, input_string, y_or_n as type_chk
from Account import Account as acc
from TwoFactorAccount import TwoFactorAuth as factor_auth


class PasswordManager:
    __all_accounts = None

    CHOICE = ["a", "v", "c", "d", "q"]

    @staticmethod
    def display_menu():
        print()
        print("Password Manager Menu:")
        print("a: Add Account")
        print("v: View List of Accounts")
        print("c: Change Password")
        print("d: Delete Account")
        print("q: Exit <== Program in prog. can only exit")
        print("--------------------")

    @classmethod
    def init(cls):
        # cls.__all_accounts = Account.read_data()
        pass

    @classmethod
    def run(cls):
        while True:
            cls.display_menu()
            choice = select_item(prompt="Please select an option:: ", error="Please select only one of the items above!", choices=cls.CHOICES)

            match choice:
                case "q":
                    break
                case "a":
                    cls.add_account()
                case "v":
                    cls.view_account_list()
                case "c":
                    cls.change_password()
                case "d":
                    cls.delete_account()

    @classmethod
    def delete_account(cls):
        pass

    @classmethod
    def add_account(cls):
        _website_name = input_string("Enter website name: ")
        _website_url = input_string("Enter website URL: ")
        _username = input_string("Enter username: ")
        _password = input_string("Enter password (or leave blank to generate a random one): ")
        _type = type_chk(prompt="Does your account have two-factor authentication enabled (yes/no)? ",
                         error="Invalid input", ge='yes', gt='y', le='no', lt='n')

        if _type:
            #
        if _password == "" or not _type:
            account = acc(website_name=_website_name, url=_website_url, username=_username, _type=_type)
            cls.accounts.append(account)
        else:
            two_auth_account = factor_auth(website_name=_website_name, url=_website_url, username=_username,
                                           password=_password)
            cls.accounts.append(two_auth_account)

        print("Account added successfully!")

    @classmethod
    def view_account_list(cls):
        if cls.accounts:
            for i, account in enumerate(self.accounts, start=1):
                print(f"\nAccount {i}:\n{account}")
        else:
            print("No accounts present to display.")

    def change_password(self):
        self.view_account_list()

        if not self.accounts:
            print("No accounts to change password")
        else:
            account_index = input_int(prompt="Enter choice (1-4): ", error="Invalid inputs.", is_float=False, le=1,
                                      ge=4)-1

            if 0 <= account_index < len(self.accounts):
                new_password = input_string(prompt="Enter the new password: ")
                self.accounts[account_index].change_password(new_password)
                print("Password changed successfully!")
            else:
                print("Invalid account number.")



