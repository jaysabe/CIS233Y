# define TwoFactorAccount
from logic.Account import Account


class TwoFactorAuth(Account):
    __account_type = ""
    __two_factor_val = ""

    def __init__(self, name, url, username, password, _type, _info, last_changed):
        super().__init__(name, url, username, password, last_changed)
        self.__account_type = _type
        self.__two_factor_val = _info

    def __str__(self):
        return super().__str__() + f" {self.__account_type}:{self.__two_factor_val}"

