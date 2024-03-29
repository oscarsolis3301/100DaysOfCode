import random

from art import logo

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_winner(user_score, computer_score):
    if 0 < user_score < 22 and 0 < computer_score < 22:
        if user_score > computer_score:
            print(f"Your score: {user_score} | Computer score: {computer_score}")
            print("You win 😁")
        elif computer_score > user_score:
            print(f"Your score: {user_score} | Computer score: {computer_score}")
            print("You lost.")
        elif user_score == computer_score:
            print(f"Your final score: {user_score} | Final computer score: {computer_score}")
            print("Draw 🙃")
    elif computer_score > 21:
        print("Opponent went over. You win!")


while True:
    user_deck = []
    computer_deck = []
    u_score = 0
    c_score = 0

    user_deck.append(random.choice(DECK))
    user_deck.append(random.choice(DECK))

    computer_deck.append(random.choice(DECK))
    computer_deck.append(random.choice(DECK))

    for cards in user_deck:
        u_score += cards

    for cards in computer_deck:
        c_score += cards
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
        print("Thank you for joining us.")
        break
    else:
        while u_score < 22 and c_score < 22:
            print(logo)
            print(f"Your cards: {user_deck}, current score: {u_score}")
            print(f"Computer's first card: {computer_deck[0]}")

            if input("Type 'y' to get another card, type 'n' to pass: ").lower() != 'y':
                check_winner(u_score, c_score)
                break
            else:
                user_deck.append(random.choice(DECK))
                computer_deck.append(random.choice(DECK))

                u_score = sum(user_deck)
                c_score = sum(computer_deck)
        if u_score > 21 > c_score:
            i = 0
            for value in user_deck:
                if value == 11:
                    user_deck[i] = 1
                i += 1
            print(f"You went over. You lose. Your score: {u_score} | Computer's score: {c_score}")
        elif c_score > 21 > u_score:
            print(f"The computer went over. You win! Your score: {u_score} | Computer's score: {c_score}")
# print(logo)
# user_total = 0
# computer_total = 0
# while user_total < 22 and computer_total < 22:
#
#     user_cards = []
#     computer_cards = []
#
#     # Giving the user their deck of cards
#     user_cards.append(random.choice(DECK))
#     user_cards.append(random.choice(DECK))
#
#     for card in user_cards:
#         user_total += card
#
#     print(f"\tYour cards: {user_cards}, current score: {user_total} ")
#
#     # Giving the computer their deck of cards
#     computer_cards.append(random.choice(DECK))
#     computer_cards.append(random.choice(DECK))
#
#     for card in computer_cards:
#         computer_total += card
#
#     print(f"\tComputer's first card: {computer_cards[0]}")
#
#     keep_going = input("Type 'y' to get another card, type  'n' to pass: ").lower()
#     if keep_going == 'n':
#
#         if 21 >= user_total > computer_total:
#             print("You win!")
#
#     elif keep_going == 'y':
#         user_cards.append(random.choice(DECK))
#
#         user_total = 0
#         for card in user_cards:
#             user_total += card
#
#         if user_total > 21:
#             print("You went over. You busted.")
#             break
