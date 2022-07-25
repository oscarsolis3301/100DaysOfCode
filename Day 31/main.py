import tkinter
from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.title("Flashcards")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='../Day 31/images/card_front.png', format='png')
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

image_right = PhotoImage(file='../Day 31/images/right.png')
image_wrong = PhotoImage(file='../Day 31/images/wrong.png')

button_right = Button(image=image_right, highlightthickness=0)
button_right.grid(row=1, column=1)

button_wrong = Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(row=1, column=0)

canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Trouve", font=("Ariel", 60, "bold"))
window.mainloop()
