alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def encrypt(plain_text, shift_amount):
    end_result = ""
    for letter in plain_text:
        if letter not in alphabet:
            end_result += letter
        else:
            if alphabet.index(letter) + shift_amount < 25:
                end_result += alphabet[alphabet.index(letter) + shift_amount]
            else:
                print("Index: " + str(shift_amount % len(alphabet)))
                end_result += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
    print(f"The new string is: {end_result}")


def decode(plain_text, shift_amount):
    end_result = ""
    for letter in plain_text:
        if letter not in alphabet:
            end_result += letter
        else:
            end_result += alphabet[alphabet.index(letter) - shift_amount]
    print(f"The new string is: {end_result}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decode(text, shift)
    continue_running = input("Would you like to try again? (\"Yes\" or \"No\"")
    if continue_running.lower() == "yes":
        continue
    elif continue_running.lower() == "no":
        break
