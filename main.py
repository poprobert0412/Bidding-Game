from art import logo
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/Mac
    else:
        _ = os.system('clear')


auction_dict = {
    "name": [],
    "bid": []
}

while True:
    print(logo)
    print("Welcome to the secret autction program.")
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    auction_dict["name"] = name
    auction_dict["bid"] = bid
    another_bidder = input("are there any other bidders? Type 'yes' or 'no': ").lower()
    while True:
        if another_bidder == 'yes':

