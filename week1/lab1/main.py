# ******************************************************************************
# Author:           Jay Abegglen
# Lab:              1
# Date:             01/15/2024
# Description:      This program is meant to test out certain validation functions using keyword args,
# optional default statements and other concepts.
#
# Input:
# Output:
# Sources:          Lab 1 specifications
#                   Module 1
# ******************************************************************************

import input_validation as test


def main():
    val1 = test.input_val("int", "Please enter a whole number greater than or equal to 0 and less than 100: ", ge=0, lt=100)
    val_float = test.input_val("float", "Please enter a decimal number between 1 and 30 inclusive: ", ge=1, le=30)
    val_float2 = test.input_val("float", "Enter a positive decimal number: ", ge=0.0)
    val_str = test.input_val("str", "Enter a string value: ", valid=lambda x: x.isalpha())
    val_bool = test.input_val("bool", "Please enter yes or no: ")
    val_selected_choice = test.input_val("choice", "Select an item: ", "Error. please try again", )


if __name__ == '__main__':
    # print(iv.input_int("Please enter a year: "))
    # print(iv.input_int(prompt="Please enter a year between 1915 and 2014", ge=1915, le=2014))
    # print(iv.input_int(prompt="Please enter a year after 1910", gt=1960))
    # print(iv.input_int("Please enter a year before 2022: ", lt=2022))
    # main()
    # print(iv.input_int("Hello! ", lt=-333))
    # not allowed: print(iv.input_int(lt=-333, "Hello! "))
    # is allowed: print(iv.input_int(lt=-333, prompt="Hello! "))
    # year = test.input_int(
    #         "Please enter a year between 1915 and 2014: ",
    #         "Year must be between 1915 and 2014!",
    #         ge=1915,
    #         le=2014
    #     )
    # test.select_item(lt=23, prompt="Hello friend", gt="Jay", le=6)
    main()
