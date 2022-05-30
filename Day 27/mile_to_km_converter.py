from tkinter import *

win = Tk()
win.minsize(width=400, height=300)
win.title("Mile to Km Converter")


def calculate():
    miles = miles_entry.get()
    km = (float(miles) * 1.609)
    converted_label.config(text=int(km))


# Entry for Miles
miles_entry = Entry()
miles_entry.config(width=10)
miles_entry.grid(column=1, row=0)

# Text for Miles
label_miles = Label(text="Miles", font=("Arial", 12, "bold"))
label_miles.grid(column=2, row=0)

# Conversion text
label_equal = Label(text="is equal to", font=("Arial", 12, "bold"))
label_equal.grid(column=0, row=1)

# Converted label
converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

# Convert Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


win.mainloop()