import smtplib
import datetime
import random
import pandas as pd

EMAIL = "OscarLearnsPython@gmail.com"
PASSWORD = "##########"

now = datetime.datetime.now()
current_day = now.weekday()

days = {0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"}

quotes_list = []

current_day_of_week = days[current_day]
random_quote = ''

list_of_birthdays = pd.read_csv("list_of_birthdays.csv")
df = pd.DataFrame(list_of_birthdays)
birthdays = df.to_dict('records')

BIRTHDAY_MONTH = 7
BIRTHDAY_DAY = 27
BIRTHDAY_YEAR = 2022

birthday = []
test_birthday = ''

# Also, I know at one point or another you'll probably see this
# So hiii beby <3
# I love you so much :)

for x in birthdays:
    for y in x:

        if type(x[y]) == int:
            test_birthday += f"{x[y]}"
            if len(test_birthday) == 7:
                birthday.append(test_birthday)
                test_birthday = ''
        else:
            pass

birthday_amount = len(birthday)

today = f'{now.year}{now.month}{now.day}'

email_of_birthday_person_thing = ''
name_of_birthday_person_thing = ''

letters = []

with open('letter_1.txt') as letter:
    letters.append(letter.read())

with open('letter_2.txt') as letter:
    letters.append(letter.read())

with open('letter_3.txt') as letter:
    letters.append(letter.read())


for x in birthday:
    if x == today:
        email_of_birthday_person_thing = birthdays[birthday.index(x)][' email'].strip()
        name_of_birthday_person_thing = birthdays[birthday.index(x)]['name']

        chosen_letter = random.choice(letters)
        edited_letter = chosen_letter.replace("[NAME]", name_of_birthday_person_thing)

        with open("quotes.txt") as quotes:
            for quote in quotes:
                quotes_list.append(quote)
            random_quote = random.choice(quotes_list)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=email_of_birthday_person_thing,
                                msg=f"Subject:Happy Birthday {name_of_birthday_person_thing}\n\n{edited_letter}")

            print(f'Email sent to {name_of_birthday_person_thing} since it is their birthday\n\n'
                  f'Email sent:\n\n{edited_letter}')


# for year in now.year:
#     for month in now.month:
#         for day in now.month:
#             for x in len(birthday):
#                 if year == birthday[x]:
#                     print('test')
