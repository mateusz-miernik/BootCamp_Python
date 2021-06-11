"""
    DAY 10: Python Calculator
"""

import os
from operations import *
from art import logo

operators_dict = {"+": add,
                  "-": subtract,
                  "*": multiply,
                  "/": divide}


def calculator():
    print(f"{logo}\n")

    first_number = float(input("What's the first number?: "))
    for key in operators_dict:
        print(key)

    should_continue = True
    while should_continue:
        operator = input("Pick an operator: ")
        second_number = float(input("What's the second number?: "))

        try:
            calculation_function = operators_dict[operator]
            result = calculation_function(first_number, second_number)
        except KeyError:
            exit_calc = input("You typed wrong operator! Press anything to continue or press '0' to exit program")
            if exit_calc == "0":
                print("Exiting...")
                break
            else:
                continue

        print(f"{first_number} {operator} {second_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, "
                           f"type 'n' to start a new calculation or press '0' to exit program.")

        if choice == "y":
            first_number = result
        elif choice == "n":
            should_continue = False
            os.system("cls")
            calculator()
        else:
            break


if __name__ == "__main__":
    calculator()
