# define TwoFactorAccount
from Account import Account
from input_validation import select_item as select_type


class TwoFactorAuth(Account):
    __account_type = ""
    __two_factor_val = ""

    def __init__(self, website_name, url, username, password, two_factor_val, _type=True):
        super().__init__(website_name, url, username, _type, password)
        self.account_type = _type
        self.__two_factor_val = two_factor_val


    @classmethod
    def set_two_factor_type(cls):
        auth_type_map = {"pin": "Pin", "secret": "Secret", "secret q": "Secret Question"}

        # Call the select_item function with the custom _map dictionary
        selected_auth_type = select_type(prompt="Enter the two-factor type: ",
                                         error="Invalid two-factor type. Please try again.",
                                         _map=auth_type_map)

        return selected_auth_type

    def __str__(self):
        # Include two-factor information in the string representation
        parent_str = super().__str__()
        return f"{parent_str}\nTwo-Factor Type: {self.account_type}\nTwo-Factor Value: {self.two_factor_val}"

