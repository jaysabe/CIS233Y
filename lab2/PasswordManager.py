# defines password manager
from input_validation import input_int, input_string, y_or_n as type_chk
from Account import Account as acc
from TwoFactorAccount import TwoFactorAuth as factor_auth

class PasswordManager:
    def __init__(self):
        self.accounts = []

    @staticmethod
    def display_menu():
        print("Password Manager Menu:")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Change Password")
        print("4. Exit <== Program in prog. can only exit")
        print("--------------------")

    def run(self):
        while True:
            self.display_menu()
            c = input_int(prompt="Enter choice (1-4): ", error="Invalid inputs.", is_float=False, le=1, ge=4)
            self.input_choice(self, c)

    def add_account(self):
        _website_name = input_string("Enter website name: ")
        _website_url = input_string("Enter website URL: ")
        _username = input_string("Enter username: ")
        _password = input_string("Enter password (or leave blank to generate a random one): ")
        _type = type_chk(prompt="Does your account have two-factor authentication enabled (yes/no)? ",
                         error="Invalid input", ge='yes', gt='y', le='no', lt='n')

        if _password == "" or not _type:
            account = acc(website_name=_website_name, url=_website_url, username=_username, _type=_type)
            self.accounts.append(account)
        else:
            two_auth_account = factor_auth(website_name=_website_name, url=_website_url, username=_username,
                                           password=_password, _type=_type)
            self.accounts.append(two_auth_account)

        print("Account added successfully!")

    def view_account_list(self):
        if not self.accounts:
            print("No accounts present to display.")
        else:
            for i, account in enumerate(self.accounts, start=1):
                print(f"\nAccount {i}:\n{account}")

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

    @staticmethod
    def input_choice(self, c):
        # if c == 1:
        #     # Add Account
        #     self.add_account()
        # if c == 2:
        #     # Check Account
        #     self.view_account_list()
        # if c == 3:
        #     # Change password
        #     self.change_password()
        if c == 4:
            # Exit Program
            print("Exiting Password Manager.")
            exit(0)


