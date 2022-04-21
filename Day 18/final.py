import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
tom.up()
turtle.colormode(255)

color_list = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (234, 226, 204), (224,
                                                                                                                234,
                                                                                                                230)]

tom.sety(-300)
for x in range(10):
    tom.setx(0)
    tom.sety(tom.ycor() + 50)
    for y in range(10):
        tom.down()
        color_choice = random.choice(color_list)
        tom.dot(20, color_choice)
        tom.up()
        tom.forward(50)


screen = Screen()
screen.exitonclick()
