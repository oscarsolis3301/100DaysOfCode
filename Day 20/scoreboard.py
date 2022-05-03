from turtle import Turtle
ALIGNMENT = "center"
FONT = ("times new roman", 8, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.up()
        self.goto(0, 280)
        self.write("Score: ", align=ALIGNMENT, font=FONT)
        self.score = Turtle()
        self.points = 0
        self.score.up()
        self.score.color("white")
        self.score.goto(20, 278)
        self.score.hideturtle()
        self.score.write(self.points)

    def add_point(self):
        self.points = self.points + 1
        self.score.clear()
        self.score.write(self.points)

