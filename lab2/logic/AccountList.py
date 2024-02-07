class AccountList:
    def __init__(self, name, security_level):
        self.__name = name
        self.__security_level = security_level
        self.__accounts = []

    def __str__(self):
        return f"<Category: {self.__name}>"

    def __iter__(self):
        return self.__accounts.__iter__()

    def __add__(self, other):
        new_name = f"{self.__name}/{other.__name}"
        new_security_level = (self.__security_level + other.security_level) / 2
        new_account_list = AccountList(new_name, new_security_level)
        new_account_list.__accounts.extend(self.__accounts + other.accounts)
        return new_account_list

    def list(self):
        print(f"Accounts in {self.__name}:")
        for account in self.__accounts:
            print(account)

    def add(self, account):
        self.__accounts.append(account)

    def remove(self, website_name, username):
        for account in self.__accounts:
            if account.website_name == website_name and account.username == username:
                self.__accounts.remove(account)
                print(f"Account for {website_name} with username {username} removed successfully.")
                return
        print("Account not found in the list.")
