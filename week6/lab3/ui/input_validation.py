# validate input functions here
from logic.Account import Account


def valid_pin_number(n):
    return len(n) == 4 and n[0:3].isdigit()


def input_range(value, gt, ge, lt, le):
    print(value, ":", gt, ge, lt, le)
    if ge is not None and value < ge:
        print(f"Value must be greater than {ge}!")
        return False
    if gt is not None and value <= gt:
        print(f"Value must be greater than or equal to {gt}!")
        return False
    if le is not None and value > le:
        print(f"Value must be less than {le}!")
        return False
    if lt is not None and value >= lt:
        print(f"Value must be less than or equal to {lt}!")
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


def is_not_empty(s):
    return len(s) > 0


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
        try:
            val = input(prompt)
            if valid(val):
                return val
            print(error)
        except ValueError:
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
    value_dict = {}
    for choice in choices:
        value_dict[choice.lower()] = choice
    if map is not None:
        for key in map:
            value_dict[key.lower()] = map[key]
    while True:
        val = input(prompt).lower()
        if val in value_dict:
            return value_dict[val]
        print(error)


def input_val(type="int", *args, **kwargs):
    # interface:
    if type == "int":
        return input_int(*args, **kwargs)
    elif type == "str":
        return input_string(*args, **kwargs)
    elif type == "float":
        return input_float(*args, **kwargs)
    elif type == "bool":
        return y_or_n(*args, **kwargs)
    elif type == "choice":
        return select_item(*args, **kwargs)
    else:
        print("Error! Unknown type:", type)


def check_site_exist(name):
    try:
        site = Account.search(name)
        if site is not None:
            print(f"A {site} account has been found. No duplicates. Returning to main menu. . .")
            return True
        else:
            return False
    except KeyError:
        pass


#  * = packs any num of positional args
# ** = packs any num of keyword args
