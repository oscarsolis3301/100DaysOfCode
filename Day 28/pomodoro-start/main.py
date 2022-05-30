from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Pomodoro")
win.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

tomato = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark = "✔"
check = Label(fg=GREEN, text=check_mark, pady=20, bg=YELLOW)
check.grid(column=1, row=2)
win.mainloop()
