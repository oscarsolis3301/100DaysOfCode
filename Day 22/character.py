from turtle import Turtle


class Character(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.up()
        self.goto(0, 0)
        self.color("white")
        print(f"currently at: {self.ycor()}")

    # def move_up(self):
    #     if 280 > self.ycor() >= -280:
    #         self.forward(20)
    #         print(f"currently at: {self.ycor()}")
    #
    #     else:
    #         pass
    #
    # def move_down(self):
    #     if 280 >= self.ycor() > -280:
    #         self.backward(20)
    #         print(f"currently at: {self.ycor()}")
    #
    #     else:
    #         pass
