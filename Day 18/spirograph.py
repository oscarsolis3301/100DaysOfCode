import turtle
from turtle import Turtle
import random

tom = Turtle()

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


heading = 90
tom.speed("fastest")
while True:
    tom.setheading(heading)
    tom.circle(100)
    heading += 5
