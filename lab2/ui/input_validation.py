# validate input functions here
from logic.Account import Account

def valid_pin_number(n):
    return len(n) == 4 and n[0:3].isdigit()


def input_range(value, gt, ge, lt, le):
    if gt is not None and value < gt:
        print(f"Value must be greater than {gt}!")
        return False
    if ge is not None and value <= ge:
        print(f"Value must be greater than or equal to {ge}!")
        return False
    if lt is not None and value > lt:
        print(f"Value must be less than {lt}!{fail}")
        return False
    if le is not None and value >= le:
        print(f"Value must be less than or equal to {le}!")
        return False
    return True


def input_int(prompt="Please enter a whole number: ", error="Invalid input. Please enter a whole number.",
              ge=None, gt=None, le=None, lt=None):
    while True:
        try:
            string = input(prompt)
            integer = int(string)
            if input_range(integer, gt, ge, lt, le):
                return integer
            print(error)
        except ValueError:
            print(error)


def input_float(prompt="Please enter a decimal: ", error="Invalid input. Please enter a floating value.",
              ge=None, gt=None, le=None, lt=None):
    while True:
        try:
            string = input(prompt)
            integer = int(string)
            if input_range(integer, gt, ge, lt, le):
                return integer
            print(error)
        except ValueError:
            print(error)


def input_string(prompt="Please enter your item name: ", error="Invalid input. Please enter valid text.", valid=lambda x: len(x) > 0):
    while True:
        val = input(prompt)
        if valid is not None and valid(val):
            return val
        else:
            print(error)


def y_or_n(prompt="Please answer with yes or no: ", error="Invalid input. Please answer with yes or no."):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["y", "yee", "yea", "yes"]:
            return True
        elif user_input in ["n", "no", "nein", "non"]:
            return False
        else:
            print(error)


def select_item(prompt="Please set a default statement here", error="Invalid input. Please try again.", choices=["Yes", "No"], map=None):
    _dict = {}

    for choice in choices:
        _dict[choice.lower()] = choice
    if map is not None:
        for key in map:
            _dict[key.lower()] = map[key]

    while True:
        user_input = input(prompt).lower()

        if user_input in _dict:
            return _dict[user_input]
        else:
            print(error)


def input_val(_type="int", *args, **kwargs):
    # interface:
    if _type == "int":
        return input_int(*args, **kwargs)
    elif _type == "str":
        return input_string(*args, **kwargs)
    elif _type == "float":
        return input_float(*args, **kwargs)
    elif _type == "bool":
        return y_or_n(*args, **kwargs)
    elif _type == "choice":
        return select_item(*args, **kwargs)
    else:
        print("Type was not properly set", _type)


def check_site_exist(name):
    try:
        site = Account.search(name)
        if site is not None:
            print(f"Site {name} already exists!")
            return True
        else:
            return False
    except KeyError:
        pass


#  * = packs any num of positional args
# ** = packs any num of keyword args
