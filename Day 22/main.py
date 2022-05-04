from enemy import Enemy
from character import Character
from ball import Ball
from turtle import Screen

screen = Screen()
screen.setup(width=60, height=60)
main_paddle = Character()

screen.bgcolor("black")
#
# screen.onkeypress(main_paddle.move_up, "Up")
# screen.onkeypress(main_paddle.move_down, "Down")
screen.listen()

screen.exitonclick()