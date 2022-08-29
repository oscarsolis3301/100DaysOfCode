from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, brain: QuizBrain):
        self.window = Tk()
        self.get_quiz = brain
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.l = Label(self.window, text="Score: 0")
        self.l.config(padx=20, pady=30, font=("Comic Sans", 20, "normal"), bg=THEME_COLOR)
        self.l.grid(column=1, row=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some question",
            fill="black", font=("Ariel", 20, "italic"),
            width=280
        )

        self.get_next_question()

        self.right = PhotoImage(file="images/true.png")
        self.right_button = Button(
            image=self.right,
            highlightthickness=0,
            command=self.correct
        )
        self.right_button.grid(padx=20, pady=50, column=0, row=2)

        self.false = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false,
            highlightthickness=0,
            command=self.wrong
        )
        self.false_button.grid(padx=20, pady=50, column=1, row=2)
        self.window.mainloop()

    def get_next_question(self):
        if self.get_quiz.still_has_questions():
            self.l.config(text=f"Score: {self.get_quiz.score}")
            question = self.get_quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct(self):
        self.give_feedback(self.get_quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.get_quiz.check_answer("False"))

    #     question = self.get_quiz.next_question()
    #     print(question)
    #     question = self.get_quiz.next_question()
    #     print(question)
    #     #self.canvas.itemconfig(self.question_text, text=question)
    #     print(question)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.right_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.canvas.after(1000, self.reset)

    def reset(self):
        self.right_button.config(state="normal")
        self.false_button.config(state="normal")
        self.get_next_question()
        self.canvas.config(bg="white")
