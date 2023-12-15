# Original code creator; Prof. Nedd (Guttman CC)
# Modified By: Christian "Cal" Lewis
# File Name: conversion.calculator.py
# Description: This file converts numbers
# from binary to decimal and decimal to binary
# The code verifies that the users has given
# a valid binary or decimal input.
# Code begins below.
######################################################################
from os import system, name

def get_digits():
# used for number conversion
    num_dict = {
            "0":0, "1":1, "2":2, "3":3, "4":4, "5":5,
            "6":6, "7":7, "8":8, "9":9, "A":10, "B":11,
            "C":12, "D":13, "E":14, "F":15
    }
    return num_dict
########################################################################

def get_menu():
# used as the primary display menu
    menu_dict = {
        '1': 'decimal_to_binary',
        '2': 'binary_to_decimal',
        'x': 'exit_program'
    }
    return menu_dict
######################################################################

def display_menu():
    menu_dict = get_menu()
# used to get results from the menu
    for items, values in menu_dict.items():
        print(items+"."+ values.replace('_',' ').capitalize())
    menu_selection = input("Enter Selection: ").lower()
    return menu_selection
#####################################################################

def clear_screen():
#This function clears the screen. It needs the OS module to be imported
# Add the following line to the top of the Code
# from os import system, name
    if name == 'nt': # clear screen syntax for windows
        _ = system('cls')
    else:
        _ = system('clear') # clear screen syntax mac
#####################################################################

def check_user_selection(items, dict):
# if user sends a blank entry
    if len(items) <1:
        input("Missing number. Try again!")
        return True
# obtain dictionary keys and place in the list
    display_list = list(dict)
#  loop through each key in display_list
    for item in items:
# check if selection in key
        if item in display_list:
            continue
        else:
            input("Invalid Selection!")
            return True
# if it gets to return item that means the number is good
    return items
######################################################################

def execute_selection(menu_selection):
# place an explanation of the function
# if menu selection is True then the user has given us a blank
# entry. We want to ignore blank entries and continue
    if menu_selection is True:
        return menu_selection, None
# this function assumes that error checking occurs elsewhere
    selection = get_menu() [menu_selection]
    return eval(selection+"()")
######################################################################

def exit_program():
    print("Good Bye!")
    return False, None
######################################################################

def decimal_to_binary():
    return True, "Binary number"
######################################################################
def binary_to_decimal():
    return True, "Decimal number"
######################################################################

def binary_to_decimal():
# Place an explanation of the function here
    convert_from = 2
    valid_numbers = list(get_digits()) [0:convert_from]
    print("Binary Digits:", valid_numbers)
    num = input("Enter a binary number: ")
    num = check_user_selection(num, valid_numbers)
    result = convert_to_decimal(num, convert_from)
    return result, "Decimal number"
#######################################################################
def convert_to_decimal(ans, conversion_number):
# Place an explanation of the function
# Exit the program if the user wants to exit. Let False continue to
# pass through functions. Otherwise perform task
    if ans is False:
        return ans
    else:
        result = 0
        if ans is True:
            return ans
        if len(ans) > 0:
# determine greatest power
             power = len(str(ans)) - 1
# start from the largest number and move to the right
             for num in str(ans):
                 calc_num = get_digits()[num]
                 result += calc_num * conversion_number ** power
                 power -= 1      # decrease by 1

             return result
##########################################################################

def decimal_to_binary():
# This function takes the digits that were based from the conversions, which
# prints out a list of valid numbers.
    convert_from = 10
    convert_to = 2
    valid_numbers = list(get_digits()) [0:convert_from]
    print("Decimal Digits:", valid_numbers)
    num = input("Enter a decimal number: ")
    num = check_user_selection(num, valid_numbers)
    result = convert_from_decimal(num, convert_to)
    return result, "Binary number"
###########################################################################

def convert_from_decimal(ans, conversion_number):
# Exit the program if user wants to exit. Let False continue to
# pass through functions. Otherwise perform task
    if ans is False:
        return(ans)
    else:
        result = ""
        if ans is True:
            return ans
        int_ans = int(ans)
        while int_ans > 0:
            remainder = int_ans % conversion_number
            int_ans = int_ans // conversion_number
            result = (list(get_digits().items())[remainder])[0] + result
        return(result)
###########################################################################

def display_selection(display, conversion_type):
    if display is False:

        return display

    elif conversion_type is None:
        return True
    else:
        if display is not True:
            input (conversion_type+': '+str(display))
    return True
#############################################################################

def main():
    menu_selection = True
    while menu_selection:
        clear_screen()
        menu_selection = display_menu()
        menu_selection = check_user_selection(menu_selection, get_menu())
        menu_selection, conversion_type = execute_selection(menu_selection)
        menu_selection = display_selection(menu_selection, conversion_type)
#####################################################################

if __name__ == "__main__":
    main()
