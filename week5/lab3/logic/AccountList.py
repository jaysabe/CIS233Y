class AccountList:
    __title = ""
    __security_lvl = ""
    __map = {}
    ALL_ACCOUNTS = "All Accounts"
    
    def __init__(self, title, security_level, accounts):
        self.__title = title
        self.__security_level = security_level
        self.__accounts = accounts
        self.__class__.__map[title.lower()] = self

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
        except:
            new_list = None
            if new_list is not None:
                raise Exception(f"Error! List {new_title} already exists!")

        average = (self.get_level() + other.get_level()) / 2  # Calculate average level
        new_list = AccountList(new_title, average,[])

        for account in self:
            if account not in new_list:
                new_list.add(account)
        for account in other:
            if account not in new_list:
                new_list.add(account)
        return new_list

    @classmethod
    def lookup(cls, title):
        return cls.__map[title.lower()]

    @staticmethod
    def read_data():
        from data.Database import Database
        # all_accounts, all_lists = Database.read_data()
        # print("All accounts:", all_accounts)
        # print("All lists:", all_lists)
        return Database.read_data()

            