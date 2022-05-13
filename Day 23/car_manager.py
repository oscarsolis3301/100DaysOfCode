from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_len=3)
        random_color = COLORS[random.randint(0, 5)]
        self.color(random_color)
        self.setheading(180)
        self.up()
        self.goto((random.randint(330, 1000)), (random.randint(-300, 300)))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)




