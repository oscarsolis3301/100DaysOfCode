from tkinter import *

window = Tk()
window.minsize(width=500, height=500)

label = Label(text="New Text")
label.grid(column=0, row=0)


def button_clicked():
    text = entry.get()
    label.config(text=f"{text}")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=3, row=3)

window.mainloop()
