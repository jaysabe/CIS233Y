# define TwoFactorAccount
from logic.Account import Account
from ui.input_validation import input_string


class TwoFactorAuth(Account):
    __account_type = ""
    __two_factor_val = ""
    AUTH = {"phone": "phone", "pin": "pin", "sq": "secret question", "secret question": "secret question"}
    AUTH_VAL = ["phone", "pin", "secret question"]

    def __init__(self, name, url, username, password, _type, _info, last_changed):
        super().__init__(name, url, username, password, last_changed)
        self.__account_type = _type
        self.__two_factor_val = _info

    def __str__(self):
        return super().__str__() + f" {self.__account_type}:{self.__two_factor_val}"

    @staticmethod
    def choice_mapping(_2fa_code_value):
        if _2fa_code_value == "phone":
            _2fa_code = input_string("Enter phone verification code: ")
        elif _2fa_code_value == "pin":
            _2fa_code = input_string("Enter PIN: ")
        elif _2fa_code_value == "secret question":
            _2fa_code = input_string("What is the name of your first pet: ")