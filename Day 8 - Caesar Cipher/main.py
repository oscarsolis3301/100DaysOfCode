from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(instruction, plain_text, shift_amount):
    if instruction == "encode":
        end_result = ""
        for letter in plain_text:
            if letter not in alphabet:
                end_result += letter
            else:
                if alphabet.index(letter) + shift_amount < 25:
                    end_result += alphabet[alphabet.index(letter) + shift_amount]
                else:
                    end_result += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        print(f"The new string is: {end_result}")
    elif instruction == "decode":
        end_result = ""
        shift_amount = shift_amount % 26
        shift_amount *= -1

        for letter in plain_text:
            if letter not in alphabet:
                end_result += letter
            else:
                end_result += alphabet[alphabet.index(letter) + shift_amount]
        print(f"The new string is: {end_result}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))
    caesar(direction, text, shift)
    continue_running = input("Would you like to try again? (\"Yes\" or \"No\"): ")
    if continue_running.lower() == "yes":
        continue
    elif continue_running.lower() == "no":
        print("Thanks for trying out the Caesar Cipher. Goodbye.")
        break
