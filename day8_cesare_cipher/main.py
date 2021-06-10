"""
    DAY 8: Cesare Cipher
"""

from string import ascii_lowercase
from art import logo

alphabet = [letter for letter in ascii_lowercase]


def caesar(message, shift_value, mode):
    converted_message = ""
    new_alphabet = alphabet[shift_value:] + alphabet[:shift_value]

    for letter in message:
        if letter != " ":
            try:
                if mode == "encode":
                    idx = alphabet.index(letter)
                    converted_message += new_alphabet[idx]
                else:
                    idx = new_alphabet.index(letter)
                    converted_message += alphabet[idx]
            except ValueError:
                print(f"Char '{letter}' is invalid! Skipping it..")
                continue
        else:
            converted_message += letter

    print(f'Here is {mode}d result: {converted_message}')


if __name__ == "__main__":
    print(logo, "\n")

    while True:
        mode_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if shift > len(alphabet):
            shift = shift % len(alphabet)

        if mode_type == "encode" or mode_type == "decode":
            caesar(message=text, shift_value=shift, mode=mode_type)
        else:
            print("You typed wrong mode type! Exiting..")
            break

        choice = input("Would you like to try again? Type 'yes' or 'no'\n")

        if choice != 'yes':
            print('Exiting...')
            break
