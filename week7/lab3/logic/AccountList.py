from logic.Account import Account


class AccountList:
    __title = ""
    __security_lvl = 0
    __map = {}
    ALL_ACCOUNTS = "All Accounts"
    
    def __init__(self, title, security_level, accounts):
        self.__title = title
        self.__security_level = security_level
        self.__accounts = accounts
        self.__class__.__map[self.get_key()] = self

    @classmethod
    def build(cls, dict):
        return AccountList(dict["title"], dict["security level"], [Account.search(key) for key in dict["accounts"]])

    def get_key(self):
        return self.__title.lower()

    def __str__(self):
        return f"<Category: {self.__title}>"

    def __iter__(self):
        return self.__accounts.__iter__()

    def __contains__(self, acc):
        return acc in self.__accounts

    def get_title(self):
        return self.__title

    def get_level(self):
        return int(self.__security_level)

    def set_title(self, new_title):
        self.__title = new_title

    def add(self, account):
        self.__accounts.append(account)
        
    def remove(self, account):
        self.__accounts.remove(account)

    def __add__(self, other):
        new_title = self.get_title() + "/" + other.get_title()
        try:
            new_list = AccountList.lookup(new_title)
            if new_list is not None:
                raise Exception(f"Error! List {new_title} already exists!")
        except KeyError:
            new_list = None
        average = (self.get_level() + other.get_level()) / 2  # Calculate average level
        new_list = AccountList(new_title, average, [])

        for account in self:
            if account not in new_list:
                new_list.add(account)
        for account in other:
            if account not in new_list:
                new_list.add(account)
        return new_list

    @classmethod
    def lookup(cls, title):
        print(title, "\n")
        cls.print_map_keys()
        try:
            return cls.__map[title.lower()]
        except KeyError:
            # Handle missing key
            raise KeyError(f"List titled '{title}' not found")

    @staticmethod
    def read_data():
        from data.Database import Database

        return Database.read_data()

    def to_dict(self):
        return {
            "_id": self.get_key(),
            "title": self.__title,
            "security level": self.__security_level,
            "accounts": [account.get_key() for account in self.__accounts]
        }

    # TODO - remove test function
    @classmethod
    def print_map_keys(cls):
        print("Printing map keys:")
        for key, value in cls.__map.items():
            print(f"Key: {key}, Title: {value.get_title()}")

    def delete(self):
        from data.Database import Database

        del self.__class__.__map[self.get_key()]
        Database.delete_list(self)

    def add_to_database(self):
        from data.Database import Database

        Database.add_list(self)


            