from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()

win.title("Password Manager")
win.config(padx=20, pady=20)
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=52).grid(row=1, column=1, columnspan=2, pady=5)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=33).grid(row=3, column=1, pady=5)

generate_button = Button(text="Generate Password", width=15).grid(row=3, column=2)

add_button = Button(text="Add", width=36).grid(row=4, column=1, columnspan=2)

win.mainloop()



# i love you in every universe -beb