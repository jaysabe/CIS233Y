# defines password manager
from ui.input_validation import input_int, select_item, input_string, y_or_n, check_site_exist
from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList
from datetime import datetime


class PasswordManager:
    __all_accounts = None
    __all_lists = None

    CHOICES = ["p", "l", "s", "a", "d", "n", "b", "i", "r", "u", "j", "q"]

    @staticmethod
    def display_menu():
        print()
        print("Options for the account manager:")
        print("  p: Print the accounts.")
        print("  l: Print the list of account types.")
        print("  s: Print the account for a selected list.")
        print("  a: Add a new account category.")
        print("  d: Delete an account category.")
        print("  n: Make a new account.")
        print("  i: Insert account into a selected list.")
        print("  r: Select a list to remove an account.")
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
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(acc)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    @classmethod
    def print_lists(cls):
        for acc_list in cls.__all_lists:
            print(acc_list.get_key())

    @classmethod
    def select_list_category(cls):
        titles = [acc_list.get_title() for acc_list in cls.__all_lists] + ["exit"]
        # print(titles)
        prompt_str = "Account Categories: "
        for title in titles:
            prompt_str += "\n\t" + title
        prompt_str += "\nPlease select a category from the list: "
        selected = select_item(prompt=prompt_str, error="Please select only a category from this list!",
                                   choices=titles)
        if selected == "exit":
            return None
        print("Selected:", selected)
        selected_list = AccountList.lookup(selected)
        return selected_list

    # helper funct
    @classmethod
    def chk_with_keys(cls, keys, prompt_str):
        for key in keys:
            prompt_str += "\n\t" + key
        prompt_str += f"\nPlease select an account from the list: "
        selected = select_item(prompt=prompt_str, error="Please select only an account from the list!", choices=keys)

        return selected

    @classmethod
    def select_account(cls, prompt, acc_list=None):
        if acc_list is None:
            acc_list = cls.__all_accounts
        keys = [acc.get_key() for acc in acc_list] + ["exit"]
        print("account key: ", keys)
        selected_key = cls.chk_with_keys(keys, prompt)
        if selected_key == "exit":
            return
        # print("Selected:", selected_key)
        selected_acc = Account.search(selected_key)
        return selected_acc

    @classmethod
    def print_selected_list(cls):
        selected_list = cls.select_list_category()
        if selected_list is None:
            return
        print(f"Accounts for {selected_list.get_title()}:")
        for acc in selected_list:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(acc)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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
            the_list.add_to_database()
            print(f"New list \"{title}\" was added!")
            return

    @classmethod
    def delete_list(cls):
        selected_list = cls.select_list_category()
        if selected_list is None:
            return
        if selected_list.get_title() == AccountList.ALL_ACCOUNTS:
            print(f"Error! Cannot delete the {AccountList.ALL_ACCOUNTS} list!")
        if selected_list not in cls.__all_lists:
            print(f"Error! Account List {selected_list.get_title()} does not exist!")
            return
        cls.__all_lists.remove(selected_list)
        selected_list.delete()

    @classmethod
    def new_account(cls):
        has_2fa = y_or_n("Do you want two-factor authentication enabled on your account (yes/no)? ")

        site_name = input_string("What is the name of the website: ")
        url = input_string(f"What is the url for {site_name}: ")
        username = input_string(f"Enter username for the {site_name} account: ")

        try:
            exists = Account.search(username)
            if exists is not None or username == cls.__all_accounts.get_key():
                print(f"The username {username} for {site_name} site already exists!")
                return
        except KeyError:
            pass
        password = input_string(f"What is the password for your {site_name} account: ")
        if has_2fa:
            selected_val = select_item("Enter authentication method (phone, pin, or secret question): ",
                                           map=TwoFactorAuth.AUTH, choices=TwoFactorAuth.AUTH_VAL)
            two_factor_type = TwoFactorAuth.choice_mapping(selected_val)

            # Create account with 2FA logic
            account = TwoFactorAuth(site_name, url, username, password, type=two_factor_type, info=selected_val,
                                        last_changed=datetime.now())
        else:
            # Create account logic
            account = Account(site_name, url, username, password, last_changed=datetime.now())
        print(account)

        cls.__all_accounts.add(account)
        account.add_to_database()
        cls.__all_accounts.add_to_database()

    @classmethod
    def remove_acc_from_list(cls):
        print()
        the_list = cls.select_list_category()
        if the_list is None:
            return
        if the_list.get_title() == AccountList.ALL_ACCOUNTS:
            print("You can't remove an account from All Accounts!")
            return
        # website and username
        account = cls.select_account(acc_list=the_list, prompt="Websites and their usernames:")
        if account is None:
            return
        if account not in the_list:
            print(f"Account {account.get_username()} is not in the List {the_list.get_title()}")
            return
        the_list.remove(account)

    @classmethod
    def insert_acc_into_list(cls):
        the_list = cls.select_list_category()
        if the_list is None:
            return
        account = cls.select_account(prompt="Account(s) available to insert: ")
        if account is None:
            return
        if account in the_list:
            print(f"Account {account.get_username()} is already in List {the_list.get_title()}!")
            return
        the_list.add(account)

    @classmethod
    def change_password(cls):
        # Select the account to then prompt password change
        account = cls.select_account(prompt="Usernames: ")
        if account is None:
            return
        new_password = input_string("Enter the new password: ")
        account.change_password(new_password)

    @classmethod
    def join_lists(cls):
        list1 = cls.select_list_category()
        list2 = cls.select_list_category()
        if list1 is None or list2 is None:
            return
        try:
            new_list = list1 + list2
        except Exception as e:
            print(e)
            return
        print(new_list)
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
                case "n":
                    cls.new_account()
                case "i":
                    cls.insert_acc_into_list()
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
