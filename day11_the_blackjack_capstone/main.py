"""
    DAY 11: The Blackjack Capstone
"""

import os
import random as r
from art import logo
from typing import List


def draw_cards(user_cards: List, computer_cards: List, cards: List, which_hand: str) -> bool:
    if which_hand == "first":
        num_of_draws = 2
        computer_cards.append(r.choice(cards))
    elif which_hand == "next":
        num_of_draws = 1
    else:
        num_of_draws = 10

    for _ in range(num_of_draws):
        if which_hand == "first" or which_hand == "next":
            user_cards.append(r.choice(cards))
            if user_cards[-1] == 11 and sum(user_cards) > 21:
                user_cards[-1] = 1
        else:
            computer_cards.append(r.choice(cards))
            if computer_cards[-1] == 11 and sum(computer_cards) > 21:
                computer_cards[-1] = 1
            elif sum(computer_cards) > 17:
                break

    if which_hand == "first" or which_hand == "next":
        print(f"\tYour cards: {user_cards}, current score {sum(user_cards)}")
        print(f"\tComputer first card: {computer_cards[0]}")
    else:
        print(f"\tYour final hand: {user_cards}, final score {sum(user_cards)}")
        print(f"\tComputer final hand: {computer_cards}, final score: {sum(computer_cards)}")

    if which_hand == "first" or which_hand == "next":
        if sum(user_cards) == 21:
            print("You win! :)")
            game_over = True
        elif sum(user_cards) > 21:
            print("You lose! :(")
            game_over = True
        else:
            game_over = False
    else:
        if sum(user_cards) == sum(computer_cards):
            print("It's a draw! :)")
        elif sum(computer_cards) > 21:
            print("You win! :)")
        elif sum(computer_cards) > sum(user_cards):
            print("You lose! :(")
        else:
            print("You win! :)")
        game_over = True
    return game_over


def main() -> None:
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    user_cards, computer_cards = [], []
    is_game_finished = False
    game_over = False
    which_hand = "first"
    initial_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if initial_choice != "y":
        exit(1)

    while not is_game_finished:
        if which_hand == "first":
            print(logo, "\n")
            game_over = draw_cards(user_cards, computer_cards, cards, which_hand)

        if game_over:
            new_round = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            if new_round == "y":
                which_hand = "first"
                user_cards.clear()
                computer_cards.clear()
                os.system("cls")
                continue
            else:
                is_game_finished = True
                print("Exiting a game.. Bye bye")
                continue

        next_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if next_choice == "y":
            which_hand = "next"
        else:
            which_hand = "final"

        game_over = draw_cards(user_cards, computer_cards, cards, which_hand)


if __name__ == "__main__":
    main()
