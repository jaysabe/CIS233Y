from PasswordManager import PasswordManager


def input_numeric(prompt="Enter value: ", error="Invalid Input. Please try again.", is_float=False, gt=None, ge=None,
                  lt=None, le=None):
    fail = " test= ❌"
    while True:
        try:
            user_input = float(input(prompt)) if is_float else int(input(prompt))

            if gt is None and ge is None and le is None and lt is None:
                # If all optionals are None, prompt the user until a valid value is provided
                return user_input

            if gt is not None and user_input <= gt:
                print(f"Value must be greater than {gt}!{fail}")

            if ge is not None and user_input < ge:
                print(f"Value must be greater than or equal to {ge}{fail}!")

            if lt is not None and user_input >= lt:
                print(f"Value must be less than {lt}!{fail}")

            if le is not None and user_input > le:
                print(f"Value must be less than or equal to {le}!{fail}")

            return user_input
        except ValueError:
            print(f"Invalid entry. Please try again{fail}")


def input_int(prompt="Please enter a whole number: ", error="Invalid input. Please enter a whole number.", **kwargs):
    fail = str(error) + " test= ❌ "
    return input_numeric(prompt, error=fail, is_float=False, **kwargs)


def input_string(prompt="Please enter your item name: ", error="Invalid input. Please enter valid text.", valid=None):
    while True:
        val = input(prompt)
        if valid is not None and valid(val):
            return val
        else:
            print(error)


