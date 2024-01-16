# validate input functions here

def input_int(prompt="Please enter a whole number: ", gt=None, ge=None, lt=None, le=None):
    # print(prompt, "\ngt:", gt, "\nge:", ge, "\nlt:", lt, "\nle:", le)
    while True:
        try:
            user_input = int(input(prompt))
            if gt is not None and user_input <= gt:
                print(F"Value must be greater than {gt}!")
                continue
            if ge is not None and user_input < ge:
                print(F"Value must be greater than or equal to {ge}!")
                continue
            if lt is not None and user_input >= lt:
                print(F"Value must be less than {lt}!")
                continue
            if le is not None and user_input > le:
                print(F"Value must be less than or equal to {le}!")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def input_float(prompt="Please enter a decimal number: ", error="Invalid input. Please enter a valid decimal number.",
                ge=None, gt=None, le=None, lt=None):
    while True:
        try:
            val = float(input(prompt))
            if ((ge is None or val >= ge) and (gt is None or val > gt) and (le is None or val <= le)
                    and (lt is None or val < lt)):
                return val
        except ValueError:
            print(error)


def input_string(prompt="Please enter a test name here: ", error="Invalid input. Please enter valid text.", valid=None):
    while True:
        val = input(prompt)
        if valid is None or valid(val):
            return val
        else:
            print(error)


def y_or_n(prompt="Please answer with yes or no: ", error="Invalid input. Please answer with yes or no."):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'yes' or user_input == 'y':
            return True
        elif user_input == 'no' or user_input == 'n':
            return False
        else:
            print(error)


def select_item(prompt="Select an item: ", error="Invalid choice. Please try again.", **kwargs):
    for key in kwargs:
        print(key, ': ', kwargs[key], sep='')


def input_val(_type, prompt, error, **kwargs):  # squishes vals into dict arg
    if _type == "int":
        return input_int(prompt, error, **kwargs)  # separates dict into values
    elif _type == "str":
        return input_string(prompt, error, **kwargs)
    elif _type == "float":
        return input_float(prompt, error, **kwargs)
    elif _type == "bool":
        return y_or_n(prompt, error, **kwargs)
    elif _type == "choice":
        return select_item(prompt, error, **kwargs)
    else:
        print("Invalid type choice. Please try again.")


    # {"m":"Monday", "mon":"Monday", "monday":"Monday", "tu":"Tuesday",
#                 "tue":"Tuesday", "tuesday":"Tuesday", "w":"Wednesday", "wed":"Wednesday",
#                 "wednesday":"Wednesday", "th":"Thursday", "thurs":"Thursday",
#                 "thursday":"Thursday", "f":"Friday", "fri":"Friday", "friday":"Friday",
#                 "s":"Saturday", "sat": "Saturday", "saturday":"Saturday", "su":"Sunday",
#                 "sun":"Sunday", "sunday":"Sunday"}


#  * = packs any num of positional args
# ** = packs any num of keyword args