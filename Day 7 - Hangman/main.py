import random
from art import stages, logo
from words import word_list

print(logo)

chosen_word = random.choice(word_list)
display = []
guesses = []
lives = 6

for x in chosen_word:
    display.append("_")


print(f"PSST!! The word is {chosen_word}")
while "_" in display and lives != 0:

    print(display)
    guess = input("Guess a letter: ").lower()
    if guess not in guesses:
        guesses.append(guess)
        count = 0
        found = False
        for letter in chosen_word:
            if letter == guess:
                display[count] = guess
                found = True
            count += 1
        if found == False:
            print("That letter is not in the word! You lose a life.")
            print(stages[lives - 1])
            lives -= 1
    else:
        print(f"You've already guessed the letter \'{guess}\'. Try a different one.")

if lives > 0:
    print(f"You have guessed all letters in the word: {chosen_word}")
else:
    print(f"You lose! The solution was: {chosen_word}")