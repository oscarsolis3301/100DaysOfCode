from tkinter import *
from tkinter import messagebox
import random
import string
import os
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    generated_password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in
                                  range(12)])
    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details you entered:"
                                                                            f" \nEmail:{email_entry.get()} \nPassword: "
                                                                            f"{password_entry.get()} \nIs it okay to save?")
        if is_okay:
            with open('data.txt', 'a') as data:
                data.write(f'{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n')
                data.flush()
                os.fsync(data.fileno())
                data.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
win = Tk()

win.title("Password Manager")
win.config(padx=20, pady=50)
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "venzeti@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, pady=5)

generate_button = Button(text="Generate Password", width=15, command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

win.mainloop()

# i love you in every universe -beb
