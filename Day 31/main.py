from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

currently_french = None
set_word = ''
timer = None
words_unknown = {}


def restart_counter():
    window.after_cancel(timer)


def change_to_french():
    global currently_french, set_word
    set_word = random.choice(list(words_unknown.keys()))
    canvas.itemconfig(word, text=set_word, fill='black')
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(card, image=card_front)
    currently_french = True


def change_to_english():
    global currently_french
    canvas.itemconfig(word, text=words_unknown[set_word], fill='white')
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(card, image=card_back)
    currently_french = False


def flip():
    global set_word, currently_french, timer
    restart_counter()
    if currently_french:
        print("Changing to english")
        change_to_english()
    else:
        print("Changing to French")
        change_to_french()
        timer = window.after(3000, flip)


def remove_known():
    global currently_french, set_word, timer
    print(currently_french)

    if currently_french:
        if set_word in words_unknown:
            restart_counter()

            print(f"removed {set_word} and {words_unknown[set_word]}")
            words_unknown.pop(set_word)

            df = pd.DataFrame.from_dict(words_unknown, orient='index')
            df.to_csv('data/words_to_learn.csv')

            change_to_french()

            timer = window.after(3000, flip)

    else:
        if set_word in words_unknown:
            print(f"removed {set_word} and {words_unknown[set_word]}")
            words_unknown.pop(set_word)

            df = pd.DataFrame.from_dict(words_unknown, orient='index')
            df.to_csv('data/words_to_learn.csv')

            set_word = random.choice(list(words_unknown.keys()))
            flip()


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
    print("Opened file")
    change_to_french()
    timer = window.after(3000, flip)
except FileNotFoundError:
    print("File was not found... Creating file")
    # --------------------------------------------- CREATING UNKNOWN WORDS FILE ------------------
    words_unknown = pd.read_csv('data/french_words.csv', index_col=0).squeeze("columns").to_dict()
    dataframe = pd.DataFrame.from_dict(words_unknown, orient="index")
    dataframe.to_csv('data/words_to_learn.csv')
    # --------------------------------------------- CREATING UNKNOWN WORDS FILE ------------------
    change_to_french()
    timer = window.after(3000, flip)

window.mainloop()
