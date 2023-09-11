import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []

for x in chosen_word:
    display.append("_")

print(display)

guess = input("Guess a letter: ").lower()

count = 0
for letter in chosen_word:
    if letter == guess:
        display[count] = guess
        print("You guess correctly.")
    else:
        print("You guess incorrectly.")
    count += 1

print(display)