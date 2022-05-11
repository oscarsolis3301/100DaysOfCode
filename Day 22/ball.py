from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.color("white")
        self.penup()
        self.touched_top = False

    def move_up(self):
        self.sety(self.ycor() + 1)
        self.setx(self.xcor() + 1)

    def move_down(self):
        self.sety(self.ycor() - 1)
        self.setx(self.xcor() + 1)

    def move(self):
        if not self.touched_top:
            if self.ycor() != 280 and -360 < self.xcor() <= 360:
                print("First if satement")
                self.move_up()
            elif self.ycor() == 280 and -360 < self.xcor() <= 360:
                print("Second if")
                self.touched_top = True
            else:
                print("else.1 statement")
        else:
            if self.ycor() != -280 and -360 < self.xcor() <= 360:
                self.move_down()
            elif self.ycor() == -280 and -360 < self.xcor() <= 360:
                self.touched_top = False
            else:
                print("else.2 statement")
