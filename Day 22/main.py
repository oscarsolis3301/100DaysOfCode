from enemy import Enemy
from character import Character
from ball import Ball
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
r_paddle = Character((350, 0))
l_paddle = Character((-350, 0))

screen.bgcolor("black")
screen.update()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


screen.listen()

screen.exitonclick()
