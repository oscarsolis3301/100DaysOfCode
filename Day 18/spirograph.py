import turtle
from turtle import Turtle, Screen
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


def draw(size):
    for _ in range(int(360/size)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size)


draw(5)
screen = Screen()
screen.exitonclick()