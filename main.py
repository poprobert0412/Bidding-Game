from art import logo
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/Mac
    else:
        _ = os.system('clear')

def bidding_game():
    auction_dict = {
    }
    while True:
        print(logo)
        print("Welcome to the secret autction program.")
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        auction_dict[name] = bid
        another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        while True:
            if another_bidder == 'yes':
                clear_console()
                break
            elif another_bidder == "no":
                max_value = max(auction_dict.values())
                max_key = max(auction_dict, key=auction_dict.get)
                print(f"The winner is {max_key} with a bid of ${max_value}")
                return
            else:
                print("Wrong input! Please type 'yes' or 'no'")
bidding_game()