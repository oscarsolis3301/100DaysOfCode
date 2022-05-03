from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.up()
        self.goto(0, 260)
        self.score = 0
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

