from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.score = 1
        self.goto(-200, 250)
        self.hideturtle()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



