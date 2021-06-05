"""
    DAY 5: Password Generator
"""

from string import ascii_letters, punctuation
import random as rand
from itertools import chain

if __name__ == "__main__":
    print("Welcome to the PyPassword Generator!")
    password_length = int(input("How many letters would you like in your password?\n"))
    num_of_symbols = int(input("How many symbols would you like?\n"))
    num_of_numbers = int(input("How many numbers would you like?\n"))

    list_with_symbols = [rand.choice(punctuation) for i in range(num_of_symbols)]
    list_with_numbers = [rand.randint(0, 9) for i in range(num_of_numbers)]
    available_length = password_length - num_of_symbols - num_of_numbers
    list_with_letters = [rand.choice(ascii_letters) for i in range(available_length)]
    password_elements = list(chain(*[list_with_symbols, list_with_numbers, list_with_letters]))
    rand.shuffle(password_elements)
    password = "".join(str(item) for item in password_elements)
    print(f"Here is your password: {password}")
