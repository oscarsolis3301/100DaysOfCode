# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

{"A": "Alfa", "B": "Bravo"}

alph = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in alph.iterrows()}
# alphabet = {letter: value for (letter, value) in alph.iterrows()}


running = True
while running:
    try:
        user_in = input("Enter a word: ")
        user_letters = [letter.upper() for letter in user_in]
        user_phonetic = [alphabet[letter] for letter in user_letters]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        for word in user_phonetic:
            print(word)
        running = False

