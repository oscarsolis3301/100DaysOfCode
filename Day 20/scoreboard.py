from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.up()

        self.high_score = 0
        with open("data.txt") as file:
            self.high_score = file.read()
        self.score = 0
        self.display_score()
        self.display_high_score()

    def display_high_score(self):
        self.goto(150, 260)
        self.write(f"High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.goto(-200, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1

        if self.score > int(self.high_score):
            with open("data.txt", "w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.clear()
        self.display_high_score()
        self.display_score()

    def game_over(self):
        self.score = 0
        self.clear()
        self.display_score()
        self.display_high_score()
        self.goto(0, 0)


