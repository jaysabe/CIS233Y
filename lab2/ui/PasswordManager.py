# defines password manager
from ui.input_validation import select_item, input_string, y_or_n
from logic.Account import Account
from logic.TwoFactorAccount import TwoFactorAuth
from logic.AccountList import AccountList


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
        selected = select_item(prompt=prompt_string, error="Please select an item from the list!", choices=urls)
        if selected == "exit":
            return None
        print("Selected:", selected)
        selected_acc = Account.lookup(selected)
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
    def add_account(cls):
        _website_name = input_string("Enter website name: ")
        _website_url = input_string("Enter website URL: ")
        _username = input_string("Enter username: ")
        _password = input_string("Enter password (or leave blank to generate a random one): ")
        _type = y_or_n(prompt="Does your account have two-factor authentication enabled (yes/no)? ",
                         error="Invalid input", ge='yes', gt='y', le='no', lt='n')

        if _password == "" or not _type:
            account = acc(name=_website_name, url=_website_url, username=_username, _type=_type)
            cls.__all_accounts.append(account)
        else:
            two_auth_account = TwoFactorAuth(name=_website_name, url=_website_url, username=_username,
                                           password=_password)
            cls.__all_accounts.append(two_auth_account)

        print("Account added successfully!")


    @classmethod
    def change_password(cls, selected_val):
        temp = y_or_n(prompt="Continue to permanently change your password (y/n)?", error="Invalid symbols. please try again.")
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
