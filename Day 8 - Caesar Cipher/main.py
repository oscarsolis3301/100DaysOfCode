alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

running = True

while (running):

   def encrypt (text, shift):
      end_result = ""
      for letter in text:
         if alphabet.index(letter) + shift < 25:
            end_result += alphabet[alphabet.index(letter)+ shift]
         else:
            end_result += alphabet[shift % len(alphabet) - 1]
      print(f"The new string is: {end_result}")


   def decode (text, shift):
      end_result = ""
      for letter in text:
         end_result += alphabet[alphabet.index(letter) - shift]
      print(f"The new string is: {end_result}")


   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

   if direction == "encode":
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      encrypt(text, shift)
   elif direction == "decode":
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      decode(text, shift)