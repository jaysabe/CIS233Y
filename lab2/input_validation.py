# validate input functions here


def input_numeric(prompt="Enter value: ", error="Invalid Input. Please try again.", is_float=False, gt=None, ge=None,
                  lt=None, le=None):
    fail = " ❌ "
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


# Example usage:

def input_int(prompt="Please enter a whole number: ", error="Invalid input. Please enter a whole number.", **kwargs):
    error = str(error) + " ❌ "
    return input_numeric(prompt, error=error, **kwargs)


def input_float(prompt="Please enter a decimal number. "
                       "Note, if a range is not provided the default range is 0.0 to 100.0: ",
                error="Invalid input. Please enter a valid decimal number.", **kwargs):
    error = str(error) + " ❌ "
    return input_numeric(prompt, error=error, **kwargs)


def input_string(prompt="Please enter your item name: ", error="Invalid input. Please enter valid text.", valid=None):
    while True:
        val = input(prompt)
        if valid is not None and valid(val):
            return val
        else:
            print(error)


def y_or_n(prompt="Please answer with yes or no: ", error="Invalid input. Please answer with yes or no.",
           ge=None, gt=None, le=None, lt=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in [ge, gt]:
            print(f"Received {user_input}, returning True")
            return True
        elif user_input in [le, lt]:
            print(f"Received {user_input}, returning False")
            return False
        else:
            print(error)


def select_item(prompt="Enter a day of the week: ", error="Invalid day of the week. Please try again.", _map=None):
    if _map is None:
        _map = {"m": "Monday", "mon": "Monday", "monday": "Monday", "t": "Tuesday",
                "tues": "Tuesday", "tuesday": "Tuesday", "w": "Wednesday", "wed": "Wednesday",
                "wednesday": "Wednesday", "th": "Thursday", "thurs": "Thursday",
                "thursday": "Thursday", "f": "Friday", "fri": "Friday", "friday": "Friday",
                "s": "Saturday", "sat": "Saturday", "saturday": "Saturday", "su": "Sunday",
                "sun": "Sunday", "sunday": "Sunday"}
        print("Please select a day of the week:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday")

    # Create a mapping of lowercase choices to their original case values
    lowercase_map = {key.lower(): value for key, value in _map.items()}

    while True:
        user_input = input(prompt).lower()

        if user_input in lowercase_map:
            selected_val = lowercase_map[user_input]
            return selected_val
        else:
            print(error)


def input_val(_type=None, prompt="Enter day: ", error="Invalid entry. Please try again", _map=None, **kwargs):
    # interface:
    if _type == "int":
        return input_int(prompt=prompt, error=error, **kwargs)
    elif _type == "str":
        return input_string(prompt=prompt, error=error, **kwargs)
    elif _type == "float":
        return input_float(prompt=prompt, error=error, **kwargs)
    elif _type == "bool":
        return y_or_n(prompt=prompt, error=error, **kwargs)
    elif _type == "choice":
        return select_item(_map=_map, prompt=prompt, error=error, **kwargs)
    else:
        print("Type was not properly set. test=❌")


#  * = packs any num of positional args
# ** = packs any num of keyword args
