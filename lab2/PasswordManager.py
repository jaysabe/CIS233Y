# defines password manager
from input_validation import select_item, input_string, y_or_n as type_chk
from Account import Account as acc
from TwoFactorAccount import TwoFactorAuth as factor_auth


class PasswordManager:
    __all_accounts = None

    CHOICES = ["a", "v", "c", "d", "q"]

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
            choice = select_item(prompt="Please select an option: ", error="Please select only one of the items above!", choices=cls.CHOICES)

            match choice:
                case "q":
                    break
                case "a":
                    pass
                    # cls.add_account()
                case "v":
                    pass
                    # cls.view_account_list()
                case "c":
                    pass
                    # cls.change_password()
                case "d":
                    pass
                    # cls.delete_account()

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

        if _password == "" or not _type:
            account = acc(name=_website_name, url=_website_url, username=_username, _type=_type)
            cls.__all_accounts.append(account)
        else:
            two_auth_account = factor_auth(name=_website_name, url=_website_url, username=_username,
                                           password=_password)
            cls.__all_accounts.append(two_auth_account)

        print("Account added successfully!")

    @classmethod
    def view_account_list(cls):
        for account in cls.__all_accounts:
            print(account.get_name())

    @classmethod
    def select_account(cls):
        # cls.view_account_list()
        names = [account.get_name() for account in cls.__all_accounts] + ["exit"]
        prompt_str = "Current List of Accounts: "
        for name in names:
            prompt_str += "\n\t" + name
        prompt_str += "\nPlease select an account to change: "

        selected_val = select_item(prompt=prompt_str, error="Please select only an account from this list!",
                                   choices=names)
        if selected_val == "exit":
            return None

        print("Selected:", selected_val)


    @classmethod
    def change_password(cls, selected_val):
        temp = type_chk(prompt="Continue to permanently change your password (y/n)?", error="Invalid symbols. please try again.")
        if not temp:
            return

        selected_account = acc.search(selected_val)
        new_password = input_string(prompt="Enter the new password: ")
        cls.accounts[selected_account].change_password(new_password)

        print("Password changed successfully!")
        return selected_account


