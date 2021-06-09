"""
    DAY 7: Hangman
"""

import random as rand
words = ['mouse', 'parrot', 'hamster', 'giraffe', 'horse']

if __name__ == "__main__":
    print(10*"-", "Welcome in the Python Hangman Game!", 10*"-")
    word = rand.choice(words)
    blanks = " ".join("_" for blank in range(len(word)))
    lives = len(word)

    while True:
        print(f"\nYour word is {blanks}")
        guess = input("Guess a letter for word: ").lower()

        if guess in word:
            blanks = blanks[:blanks.find(guess)] + guess + blanks[blanks.find(guess)+1:]
            print("You guessed a letter!")
            if "_" not in blanks:
                print("You win! Congratulations!")
                break
        else:
            print("Wrong choice, You miss a life!")
            lives -= 1
            if lives == 0:
                print("You lose! Game Over.")
                print(f"Secret word was {word}")
                break
