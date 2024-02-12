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
        print("  s: Print the account for a selected list.")
        print("  a: Add a new List genre.")
        print("  d: Delete a list genre.")
        print("  m: Make a new account.")
        print("  i: Insert account into a list.")
        print("  r: Remove an account from a list.")
        print("  u: Update password for an account.")
        print("  j: Join two account lists together.")
        print("  q: Exit the program.")
        print("--------------------")

    @classmethod
    def init(cls):
        cls.__all_accounts, cls.__all_lists = AccountList.read_data()

    @classmethod
    def print_accounts(cls):
        for acc in cls.__all_accounts:
            print()
            print(acc)

    @classmethod
    def print_lists(cls):
        for acc_list in cls.__all_lists:
            print(acc_list.get_title())

    @classmethod
    def select_list_genre(cls):
        titles = [acc_list.get_title() for acc_list in cls.__all_lists] + ["exit"]
        prompt_str = "Credential Genres: "
        for title in titles:
            prompt_str += "\n\t" + title
        prompt_str += "\nPlease select genre from the list: "
        selected = select_item(prompt=prompt_str, error="Please select only a genre from this list!",
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
        print(f"Accounts for {selected_list.get_title()}:")
        for acc in selected_list:
            print("\t", acc)

    @classmethod
    def new_list(cls):
        while True:
            title = input_string("Please enter the name for the new list: ")
            try:
                the_list = AccountList.lookup(title)
                if the_list is not None:
                    print(f"Error! List {title} already exists")
                    continue
            except KeyError:
                pass
            if title.lower() == "exit":
                return
            security = input_int("Enter security level for the new list (1-10): ", le=10, ge=1)
            the_list = AccountList(title, security, [])
            cls.__all_lists.append(the_list)
            print(f"New list \"{title}\" was added!")
            return

    @classmethod
    def delete_list(cls):
        selected_list = cls.select_list_genre()
        if selected_list is None:
            return
        if selected_list.get_title() == AccountList.ALL_ACCOUNTS:
            print(f"Error! Cannot delete the {AccountList.ALL_ACCOUNTS} list!")
        if selected_list not in cls.__all_lists:
            print(f"Error! Account List {selected_list.get_title()} does not exist!")
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
                _2fa_type = TwoFactorAuth.choice_mapping(selected_val)

                # Create account with 2FA logic
                TwoFactorAuth(name, _url, _username, _password, _type=_2fa_type, _info=selected_val, last_changed=datetime.now())
            else:
                # Create account logic
                Account(name, _url, _username, _password, last_changed=datetime.now())
        except KeyError:
            print(f"An error occurred while searching for the account.")

    @classmethod
    def insert(cls):
        the_list = cls.select_list_genre()
        if the_list is None:
            return
        account = cls.select_account()
        if account is None:
            return
        if account in the_list:
            print(f"Account connected to {account.get_url()} is already in List {the_list.get_title()}!")
            return
        the_list.add(account)


    @classmethod
    def remove_acc_from_list(cls):
        the_list = cls.select_list_genre()
        if the_list is None:
            return
        if the_list.get_title() == AccountList.ALL_ACCOUNTS:
            print("You can't remove an account from All Accounts!")
            return
        # website and url
        account = cls.select_account(the_list)
        if account is None:
            return
        if account not in the_list:
            print(f"Account connected to {account.get_url()} is not in the List {the_list.get_title()}")
            return
        the_list.remove(account)

    @classmethod
    def change_password(cls):
        # Select the account to then prompt password change
        account = cls.select_account()
        if account is None:
            return
        new_password = input_string("Enter the new password: ")
        account.change_password(new_password)

    @classmethod
    def join_lists(cls):
        list1 = cls.select_list_genre()
        list2 = cls.select_list_genre()
        print(list1, list2)
        if list1 is None or list2 is None:
            return
        try:
            print(list1, list2)
            new_list = list1 + list2
            new_list_title = input_string("What is the name of this new list? ")
        except Exception as e:
            print(e)
            return
        new_list.set_title(new_list_title)
        cls.__all_lists.append(new_list)

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
                    cls.print_accounts()
                case "l":
                    cls.print_lists()
                case "s":
                    cls.print_selected_list()
                case "a":
                    cls.new_list()
                case "d":
                    cls.delete_list()
                case "m":
                    cls.new_account()
                case "i":
                    cls.insert()
                case "r":
                    cls.remove_acc_from_list()
                case "u":
                    cls.change_password()
                case "j":
                    cls.join_lists()

        print("Entering sleep...")


if __name__ == '__main__':
    PasswordManager.init()
    PasswordManager.run()
