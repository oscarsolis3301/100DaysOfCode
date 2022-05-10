from turtle import Turtle, Screen


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.tracer(0)
        self.speed("fastest")
        self.up()
        self.goto(380, 0)
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.shape("square")
        self.color("white")
        print(f"currently at: {self.ycor()}")

    def move_up(self):
        if 260 > self.ycor() >= -260:
            self.forward(20)
            print(f"currently at: {self.ycor()}")
            self.screen.update()
        else:
            pass

    def move_down(self):
        if 260 >= self.ycor() > -260:
            self.backward(20)
            print(f"currently at: {self.ycor()}")
            self.screen.update()
        else:
            pass
