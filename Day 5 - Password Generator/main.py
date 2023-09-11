# This program generates a random password for the user depending on their criteria

import random

print("Welcome to the PyPassword Generator")
letters_amount = int(input("How many letters would you like in your password? "))
symbols_amount = int(input("How many symbols would you like? "))
numbers_amount = int(input("How many numbers would you like? "))
total = letters_amount + symbols_amount + numbers_amount

alphabet = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 
            'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 
            'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 
            'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
symbols = ['!', '@', '#', '$']
password = ''

for letters in range(letters_amount):
    password += alphabet[random.randint(0, len(alphabet) - 1)]

for symbol in range(symbols_amount):
    password += symbols[random.randint(0, len(symbols) - 1)]

for number in range(numbers_amount):
    password += str(random.randint(0, 9))

password = ''.join(random.sample(password, len(password)))

print(f'Here is your password: {password} | Length: {len(password)}')