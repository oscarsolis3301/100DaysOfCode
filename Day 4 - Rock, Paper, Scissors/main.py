from computer_choice import computer
from art import *

running = True

def game_logic(user, computer, u_score, c_score):
    if (user == computer):
        print("\nTIE GAME")
    elif (user_choice == 0 and computer == 1):
        print(f"You chose\nROCK\n{rock}\nThe computer chose\nPAPER\n{paper}\n\nYOU LOST!")

    elif (user == 0 and computer == 2):
        print(f"You chose\nROCK\n{rock}\nThe computer chose\nSCISSORS\n{scissors}\n\nYOU WIN!")

    elif (user == 1 and computer == 0):
        print(f"You chose\nPAPER\n{paper}\nThe computer chose\nROCK\n{rock}\n\nYOU WIN!")

    elif (user == 1 and computer == 2):
        print(f"You chose\nPAPER\n{paper}\nThe computer chose\n SCISSORS\n{scissors}\n\nYOU LOST!")

    elif (user == 2 and computer == 0):
        print(f"You chose\nSCISSORS\n{scissors}\nThe computer chose\n{rock}\n\nYOU LOST!")

    elif (user == 2 and computer == 1):
        print(f"You chose\nSCISSORS\n{scissors}\nThe computer chose\nPAPER\n{paper}\n\nYOU WIN!")


while(running):
    computer_choice = computer()
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors "))
    game_logic(user_choice, computer_choice)