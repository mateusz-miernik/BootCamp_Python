"""
    DAY 12: Number Guessing Game
"""

import random as rand
from art import logo


def play_game() -> None:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking about number between 1 and 100.")
    secret_number = rand.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        number_of_tries = 10
    else:
        number_of_tries = 5

    while number_of_tries > 0:
        print(f"You have {number_of_tries} attempts remaining to guess the number.")
        your_guess = int(input("Make a guess: "))
        number_of_tries -= 1

        if your_guess == secret_number:
            print("You guessed the number! Congratulations! :)")
            break
        elif your_guess > secret_number:
            print("Too high.")
        else:
            print("Too low.")

    if number_of_tries == 0:
        print("No more attempts available in this round!")
    choice = input("Wanna play again? Choose 'yes' to play or anything else to exit program: ")

    if choice == 'yes':
        print('\n')
        play_game()
    else:
        print("Thank you, bye bye..")
        exit(1)


if __name__ == "__main__":
    play_game()
