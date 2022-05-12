from turtle import Turtle, Screen


class Character(Turtle):
    def __init__(self, location):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.speed("fastest")
        self.up()
        self.goto(location)
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.shape("square")
        self.color("white")

    def move_up(self):
        if 240 > self.ycor() >= -240:
            self.forward(20)
        else:
            pass

    def move_down(self):
        if 240 >= self.ycor() > -240:
            self.backward(20)
        else:
            pass
