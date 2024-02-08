# defines password manager
from ui.input_validation import input_int, select_item, input_string, y_or_n, check_site_exist
from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList
from datetime import datetime


class PasswordManager:
    __all_accounts = None
    __all_lists = None

    CHOICES = ["p", "l", "s", "a", "d", "b", "i", "r", "u", "j", "q"]

    @staticmethod
    def display_menu():
        print()
        print("Options for the account manager:")
        print("  p: Print the accounts.")
        print("  l: Print the list of accounts.")
        print("  s: Print the account for a selected category.")
        print("  a: Add a new category.")
        print("  d: Delete a category.")
        print("  m: Make a new account.")
        print("  i: Insert account into category.")
        print("  r: Remove an account from a category.")
        print("  u: Update the security level for an account.")
        print("  j: Join two account lists together.")
        print("  q: Exit the program.")
        print("--------------------")

    @classmethod
    def init(cls):
        cls.__all_accounts, cls.__all_account_lists = AccountList.read_data()

    @classmethod
    def print_accounts(cls):
        for acc in cls.__all_accounts:
            print(acc)

    @classmethod
    def print_lists(cls):
        for acc_list in cls.__all_lists:
            print(acc_list.get_title())

    @classmethod
    def select_list_genre(cls):
        titles = [acc_list.get_name() for acc_list in cls.__all_lists] + ["exit"]
        prompt_str = "Current List of account genres: "
        for title in titles:
            prompt_str += "\n\t" + title
        prompt_str += "\nPlease select an item from the list: "
        selected = select_item(prompt=prompt_str, error="Please select only an item from this list!",
                                   choices=titles)
        if selected == "exit":
            return None

        print("Selected:", selected)
        selected_list = AccountList.lookup(selected)
        return selected_list

    @classmethod
    def select_account(cls, acc_list=None):
        if acc_list is None:
            acc_list = cls.__all_accounts
        urls = [acc.get_url() for acc in acc_list] + ["exit"]
        prompt_str = "Current list of Accounts"
        for url in urls:
            prompt_str += "\n\t" + url
        prompt_str += "\nPlease select an item from the list: "
        selected = select_item(prompt=prompt_str, error="Please select an item from the list!", choices=urls)
        if selected == "exit":
            return None
        print("Selected:", selected)
        selected_acc = Account.search(selected)
        return selected_acc

    @classmethod
    def print_selected_list(cls):
        selected_list = cls.select_list_genre()
        if selected_list is None:
            return
        print(f"Accounts for {selected_list.get_name()}:")
        for acc in selected_list:
            print("\t", acc)

    @classmethod
    def new_list(cls):
        while True:
            name = input_string("Please enter the name for the new list: ")
            try:
                the_list = AccountList.lookup(name)
                if the_list is not None:
                    print(f"Error! List {name} already exists")
                    continue
            except KeyError:
                pass
            if name.lower() == "exit":
                return
            security = input_int("Enter security level for the new list (1-10)", le=1, ge=10)
            the_list = AccountList(name, security, [])
            cls.__all_lists.append(the_list)
            print(f"New list {name} was added!")
            return

    @classmethod
    def delete_list(cls):
        selected_list = cls.select_list_genre()
        if selected_list is None:
            return
        if selected_list.get_name() == AccountList.ALL_ACCOUNTS:
            print(f"Error! Cannot delete the {AccountList.ALL_ACCOUNTS} list!")
        if selected_list not in cls.__all_lists:
            print(f"Error! Account List {selected_list.get_name()} does not exist!")
            return
        cls.__all_lists.remove(selected_list)

    @classmethod
    def new_account(cls):
        has_account = y_or_n("Do you have an account with us (y/no?")
        if has_account:
            name = input_string("What is the name of the website: ")
            exists = check_site_exist(name)
            if exists:
                return
            has_security = y_or_n("Does your account have two-factor authentication enabled (yes/no)? ")
            if has_security:
                # call enumerate type of auth
                cls.create_account(two_factor_auth=True)
            else:
                cls.create_account()
        else:
            cls.create_new_account()
            print("Account added successfully!")

    @classmethod
    def create_new_account(cls):
        cls.create_account()

    @staticmethod
    def create_account(two_factor_auth=False):
        try:
            name = input_string("What is the name of the website: ")
            account = Account.search(name)
            if account is not None:
                print(f"Account {name} already exists!")
                return
            _url = input_string("Enter the url for the website: ")
            _username = input_string("Enter username for the account: ")
            _password = input_string("Enter password for the account: ")
            if two_factor_auth:
                selected_val = select_item("Enter authentication method (phone, pin, or secret question): ", map=TwoFactorAuth.AUTH, choices=TwoFactorAuth.AUTH_VAL)
                TwoFactorAuth.choice_mapping(selected_val)

                # Create account with 2FA logic
                TwoFactorAuth(name, _url, _username, _password, _info=selected_val, last_changed=datetime.now())
            else:
                # Create account logic
                Account(name, _url, _username, _password, last_changed=datetime.now())
        except KeyError:
            print("An error occurred while searching for the account.")

# _________________________________________________________________________________
    @classmethod
    def change_password(cls, selected_val):
        temp = y_or_n("Continue to permanently change your password (y/n)?")
        if not temp:
            return

        selected_account = Account.search(selected_val)
        new_password = input_string(prompt="Enter the new password: ")
        cls.accounts[selected_account].change_password(new_password)

        print("Password changed successfully!")
        return selected_account

    @classmethod
    def run(cls):
        while True:
            cls.display_menu()
            choice = select_item(prompt="Please select an option: ", error="Please select only one of the items above!",
                                 choices=cls.CHOICES)
            match choice:
                case "q":
                    break
                case "p":
                    pass
                    # cls.print_accounts()
                case "l":
                    pass
                    # cls.view_account_list()
                case "s":
                    pass
                    # cls.print_selected_list()
                case "a":
                    pass
                    # cls.new_list()
                case "d":
                    pass
                    # cls.delete_list()
                case "m":
                    pass
                    # cls.new_account()
                case "i":
                    pass
                    # cls.insert()
                case "r":
                    pass
                    # cls.remove_acc_from_list()
                case "u":
                    pass
                    # cls.update_security()
                case "j":
                    pass
                    # cls.join_lists()
        print("Entering sleep...")
