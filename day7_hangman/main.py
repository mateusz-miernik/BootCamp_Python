"""
    DAY 7: Hangman
"""

import random as rand
from hangman_art import stages, logo, winner, loser
from hangman_words import word_list
import os

game_is_finished = False

if __name__ == "__main__":
    print(logo, "\n")
    print(10*"-", "Welcome in the Python Hangman Game!", 10*"-")
    word = rand.choice(word_list)
    secret_word = ["_" for blank in range(len(word))]
    lives = 6

    print(stages[lives-1])
    while not game_is_finished:
        print(f"\nYour word is {' '.join(letter for letter in secret_word)}")
        guess = input("Guess a letter for word: ").lower()
        print(f"Your guess is '{guess}'")
        os.system('cls')

        if guess != "" and guess in word and guess not in secret_word:

            for idx, letter in enumerate(word):
                if guess == letter:
                    secret_word[idx] = guess

            print("You guessed a letter!")
            if "_" not in secret_word:
                print(f"\n{winner}\nCongratulations!")
                print(f"Secret word was '{word}'.")
                game_is_finished = True
        else:
            print("Wrong choice, You miss a life!")
            lives -= 1
            if lives == 0:
                print(f"\n{loser}\nGame Over.")
                print(f"Secret word was '{word}'")
                game_is_finished = True

        print(stages[lives])

    exit_program = input("Press any key to exit.. ")
