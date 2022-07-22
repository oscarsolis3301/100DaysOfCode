from tkinter import *
from tkinter import messagebox
import random
import string
import json
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
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as data:
                file_data = json.load(data)

        except FileNotFoundError:
            with open('data.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            file_data.update(new_data)

            with open('data.json', 'w') as data:
                json.dump(file_data, data, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

def Search():
    try:
        with open('data.json', 'r') as data:
            file_data = json.load(data)
            found = False
            for websites in file_data:
                if websites == website_entry.get():
                    found = True
                else:
                    continue

            if found:
                messagebox.showinfo(title=f"{website_entry.get()}",
                                    message=f"Email: {file_data[website_entry.get()]['email']}"
                                            f"\nPassword: {file_data[website_entry.get()]['password']}")
            else:
                messagebox.showinfo(title=f"{website_entry.get()}", message="The website entered was not found.")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Was Found.")


win = Tk()

win.title("Password Manager")
win.config(padx=20, pady=50)
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=Search)
search_button.grid(row=1, column=2)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = Entry(width=59)
email_entry.grid(row=2, column=1, pady=5, columnspan=2)
email_entry.insert(0, "venzeti@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, pady=5)

generate_button = Button(text="Generate Password", width=15, command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

win.mainloop()

# i love you in every universe -beb
