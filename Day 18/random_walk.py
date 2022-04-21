import turtle
from turtle import Turtle, Screen
import random

t = Turtle()
turtle.colormode(255)
moving = True


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


choices = ["left", "right", "up", "down"]


def random_movement():
    return str(random.choice(choices))


def move_right():
    t.setheading(0)
    t.forward(25)


def move_left():
    t.setheading(180)
    t.forward(25)


def move_up():
    t.setheading(90)
    t.forward(25)


def move_down():
    t.setheading(270)
    t.forward(25)


movements = {
    "right": move_right,
    "left": move_left,
    "up": move_up,
    "down": move_down,
}

t.pensize(10)

while True:
    t.pencolor(random_color())
    movements[random_movement()]()
#

#
# choices = [move_down(), move_left(), move_up(), move_down()]
#


#
# for _ in range(10):
#     random.choice(movements)
#     t.color(random.choice(colors))

screen = Screen()
screen.exitonclick()
