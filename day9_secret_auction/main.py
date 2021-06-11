"""
    DAY 9: Secret Auction
"""

import os
from art import logo

is_auction_finished = False

if __name__ == "__main__":
    print(f"{logo}\n")
    print("Welcome in the Secret Auction program!")
    auction_data = {}

    while not is_auction_finished:
        name = input("Type a name of participant:\n")
        bid_price = int(input("How much $ to bid?\n"))
        auction_data[name] = bid_price

        more_participants = input("Are there more participants to bid? Type 'yes' or 'no'.\n")
        if more_participants == "yes":
            os.system("cls")
            continue
        else:
            max_bid = max(auction_data.values())
            winner = [key for key, val in auction_data.items() if val == max_bid]

            if len(winner) == 1:
                winner = winner[0]
                print(f"The winner is {winner} with bid equal {auction_data[winner]}$")
            else:
                print("\nThere is no winner, some people bid the same price. They are:")
                for person in winner:
                    print(f"{person} with bid {auction_data[person]}$")
            is_auction_finished = True
            print("\nAuction is finished! Thanks for your attendance. See you next time.")
