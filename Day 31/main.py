from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

French, clicked = True, True
set_word = ''
timer = None
words_unknown = {}


def restart_counter():
    window.after_cancel(timer)


def french():
    global French, set_word
    French = False
    canvas.itemconfig(word, text=set_word)
    canvas.itemconfig(language, text='French')
    canvas.itemconfig(card, image=card_front)


def flip():
    global set_word, French, timer
    # window.after_id = None
    restart_counter()
    if French:
        set_word = random.choice(list(words_unknown.keys()))
        french()
        French = False
        # recount = window.after(3000, flip)
        timer = window.after(3000, flip)
    else:
        canvas.itemconfig(word, text=words_unknown[set_word], fill='white')
        canvas.itemconfig(language, text='English', fill='white')
        canvas.itemconfig(card, image=card_back)
        French = True


def remove_known():
    global set_word
    if set_word in words_unknown:
        print(f"removed {set_word}")
        words_unknown.pop(set_word)
        flip()
    else:
        print(f"{set_word} NOT FOUND")
        print(words_unknown)
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


# ------------------ UI ------------------------------------------------
window.title("Flashcards")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

# ------------------ IMAGES ------------------------------------------------
card_front = PhotoImage(file='../Day 31/images/card_front.png')
card_back = PhotoImage(file='../Day 31/images/card_back.png')
card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
image_right = PhotoImage(file='../Day 31/images/right.png')
image_wrong = PhotoImage(file='../Day 31/images/wrong.png')
# ------------------ IMAGES ------------------------------------------------


# ------------------ BUTTONS ------------------------------------------------
button_right = Button(image=image_right, highlightthickness=0, command=remove_known)
button_right.grid(row=1, column=1)
button_wrong = Button(image=image_wrong, highlightthickness=0, command=flip)
button_wrong.grid(row=1, column=0)
# ------------------ BUTTONS ------------------------------------------------


language = canvas.create_text(400, 150, text='', font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))
# ------------------ UI ------------------------------------------------


try:
    words_unknown = pd.read_csv('data/words_to_learn.csv', index_col=0).squeeze('columns').to_dict()
    set_word = random.choice(list(words_unknown.keys()))
    print(set_word)
    print("Opened file")
    french()
    timer = window.after(3000, flip)
except FileNotFoundError:
    print("File was not found... Creating file")
    # --------------------------------------------- CREATING UNKNOWN WORDS FILE ------------------
    words_unknown = pd.read_csv('data/french_words.csv', index_col=0).squeeze("columns").to_dict()
    dataframe = pd.DataFrame.from_dict(words_unknown, orient="index")
    dataframe.to_csv('data/words_to_learn.csv')
    # --------------------------------------------- CREATING UNKNOWN WORDS FILE ------------------

    print(f'List of the words unknown: ')
    for key, item in words_unknown.items():
        print(key, item)

    # set_word = random.choice(list(unknown_words.keys()))
    # words_unknown = unknown_words
    set_word = random.choice(list(words_unknown.keys()))
    canvas.itemconfig(word, text=set_word)
    canvas.itemconfig(language, text='French')
    canvas.itemconfig(card, image=card_front)
    French = False
    # recount = window.after(3000, flip)
    timer = window.after(3000, flip)

window.mainloop()
