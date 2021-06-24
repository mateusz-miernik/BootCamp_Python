"""
    DAY 14: Higher Or Lower Game
"""

import random as rand
from art import logo, vs
from game_data import data


def play_game() -> None:
    print(logo)
    score = 0

    while True:
        first_object = rand.choice(data)
        print(f"Compare A: {first_object['name']}, {first_object['description']} from {first_object['country']}")
        print(vs)
        second_object = rand.choice(data)
        print(f"Compare B: {second_object['name']}, {second_object['description']} from {second_object['country']}")
        your_guess = input("Type 'A' if you think first person has more followers "
                           "or 'B' if you think second one is more famous: ")

        if first_object['follower_count'] > second_object['follower_count']:
            if your_guess.lower() == 'a':
                print('You guessed right!\n')
                score += 1
            else:
                print('Wrong answer!\n')
                break
        else:
            if your_guess.lower() == 'b':
                print('You guessed right!\n')
                score += 1
            else:
                print('Wrong answer!\n')
                break

    print(f"You get {score} in this round.")
    if score > 5:
        print("You are a good player! :)")
    else:
        print("Your score is embarrassing! :(")

    more_game = input("Do you wanna play again? Type 'y' if yes or anything else if not: ")

    if more_game == 'y':
        play_game()
    else:
        print("Thank you, bye bye..")
        exit(1)


if __name__ == "__main__":
    play_game()
