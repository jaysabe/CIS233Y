# define TwoFactorAccount
from logic.Account import Account
from ui.input_validation import input_string


class TwoFactorAuth(Account):
    __account_type = ""
    __two_factor_val = ""
    AUTH = {"phone": "phone", "pin": "pin", "sq": "secret question", "secret question": "secret question"}
    AUTH_VAL = ["phone", "pin", "secret question"]

    def __init__(self, name, url, username, password, type, info, last_changed):
        super().__init__(name, url, username, password, last_changed)
        self.__account_type = type
        self.__two_factor_val = info

    def __str__(self):
        return super().__str__() + f" {self.__account_type}:{self.__two_factor_val}"

    def to_dict(self):
        dict = super().to_dict()
        dict["authentication"] = "TwoFactorAccount"
        dict["type"] = self.__account_type
        dict["value"] = self.__two_factor_val
        return dict

    @staticmethod
    def choice_mapping(_2fa_code_value):
        _2fa_code = ""
        if _2fa_code_value == "phone":
            _2fa_code = input_string("Enter phone verification code: ")
        elif _2fa_code_value == "pin":
            _2fa_code = input_string("Enter PIN: ")
        elif _2fa_code_value == "secret question":
            _2fa_code = input_string("What is the name of your first pet: ")

        return _2fa_code
