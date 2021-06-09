"""
    DAY 8: Cesare Cipher
"""

from string import ascii_lowercase

alphabet = [letter for letter in ascii_lowercase]


def encrypt(message, shift_value):
    encrypted_message = ""
    new_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    for letter in message:
        if letter != " ":
            idx = alphabet.index(letter)
            encrypted_message += new_alphabet[idx]
        else:
            encrypted_message += letter

    print(f'Encrypted message is: {encrypted_message}')


def decrypt(message, shift_value):
    decrypted_message = ""
    new_alphabet = alphabet[shift_value:] + alphabet[:shift_value]
    for letter in message:
        if letter != " ":
            idx = new_alphabet.index(letter)
            decrypted_message += alphabet[idx]
        else:
            decrypted_message += letter

    print(f'Decrypted message is: {decrypted_message}')


if __name__ == "__main__":

    while True:
        mode_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if mode_type == "encode":
            encrypt(text, shift)
        elif mode_type == "decode":
            decrypt(text, shift)
        else:
            break

        choice = input("Would you like to try again? Type 'yes' or 'no'\n")

        if choice != 'yes':
            print('Exiting...')
            break
