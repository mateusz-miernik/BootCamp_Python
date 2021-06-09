"""
    DAY 7: Hangman
"""

import random as rand

you_win = """
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
"""

words = ['mouse', 'parrot', 'hamster', 'giraffe', 'horse']

if __name__ == "__main__":
    print(10*"-", "Welcome in the Python Hangman Game!", 10*"-")
    word = rand.choice(words)
    secret_word = ["_" for blank in range(len(word))]
    lives = len(word)

    while True:
        print(f"\nYour word is {' '.join(letter for letter in secret_word)}")
        guess = input("Guess a letter for word: ").lower()

        if guess is not "" and guess in word and guess not in secret_word:
            print(f"Your guess is '{guess}'")
            for idx, letter in enumerate(word):
                if guess == letter:
                    secret_word[idx] = guess

            print("You guessed a letter!")
            if "_" not in secret_word:
                print(f"{you_win}\nCongratulations!")
                print(f"Secret word was '{word}'.")
                break
        else:
            print("Wrong choice, You miss a life!")
            lives -= 1
            if lives == 0:
                print("You lose! Game Over.")
                print(f"Secret word was {word}")
                break
