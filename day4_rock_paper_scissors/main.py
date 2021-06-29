"""
    DAY 4: Rock Paper Scissors
"""

import random as rand

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

if __name__ == "__main__":
    print(10*"-", "Welcome in Rock Paper Scissors python game!", 10*"-")

    while True:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

        if user_choice < 0 or user_choice >= 3:
            print("You typed invalid number! Try again..")
            continue
        else:
            computer_choice = rand.randint(0, 2)
            print("\nYou choose:")
            print(game_images[user_choice])
            print("\nComputer chose:")
            print(game_images[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                print("You win! Congratulations!")
                break
            elif computer_choice > user_choice:
                print("You lose..")
                break
            elif user_choice == 2 and computer_choice == 0:
                print("You lose..")
                break
            elif user_choice > computer_choice:
                print("You win! Congratulations!")
                break
            elif user_choice == computer_choice:
                print("It's a draw! Try again..")
                continue
