import os
from art import logo

print(f"{logo}\n")
print("Welcome to the secret auction program\n")

bidders = {}

while True:
    name = input("What is your name?: ")
    bid = input("What's your bid?: $")
    bidders[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    if others.lower() == "no":
        break
largest_bidder = max(bidders, key=bidders.get)
largest_bid = max(bidders.values())
print(f"The largest bidder is {largest_bidder} with a bid of ${largest_bid}")


