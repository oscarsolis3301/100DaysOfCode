from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

d = pd.read_csv('data/french_words.csv', index_col=0).squeeze("columns").to_dict()
french_word = random.choice(list(d.keys()))
French, clicked = True, True
set_word = ''
timer = None


def restart_counter():
    window.after_cancel(timer)


def flip():
    global set_word, French, timer
    # window.after_id = None
    restart_counter()
    if French:
        new_french_word = random.choice(list(d.keys()))
        canvas.itemconfig(word, text=new_french_word)
        canvas.itemconfig(language, text='French')
        set_word = new_french_word

        canvas.itemconfig(card, image=card_front)
        French = False
        # recount = window.after(3000, flip)
        timer = window.after(3000, flip)
    else:
        canvas.itemconfig(word, text=d[set_word])
        canvas.itemconfig(language, text='English')
        canvas.itemconfig(card, image=card_back)
        French = True

    # restart_counter()

# current_word = ''
#
#
# def display_english():
#     global French, current_word
#     French = False
#     canvas.itemconfig(language, text='English')
#     canvas.itemconfig(word, text=d[word])
#
#
# def display_french():
#     global French, current_word
#     French = True
#     canvas.itemconfig(language, text='French')
#
#
# def get_word():
#     global French, current_word
#
#     new_french_word = random.choice(list(d.keys()))
#     canvas.itemconfig(word, text=new_french_word)
#
#     current_word = new_french_word
#
#     if French:
#         display_english()
#     else:
#         display_french()


window.title("Flashcards")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file='../Day 31/images/card_front.png')
card_back = PhotoImage(file='../Day 31/images/card_back.png')

card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

image_right = PhotoImage(file='../Day 31/images/right.png')
image_wrong = PhotoImage(file='../Day 31/images/wrong.png')

button_right = Button(image=image_right, highlightthickness=0, command=flip)
button_right.grid(row=1, column=1)

button_wrong = Button(image=image_wrong, highlightthickness=0, command=flip)
button_wrong.grid(row=1, column=0)

language = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))

timer = window.after(3000, flip)

flip()

window.mainloop()
