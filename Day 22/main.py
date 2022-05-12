from scoreboard import Scoreboard
from character import Character
from ball import Ball
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Character((350, 0))
l_paddle = Character((-350, 0))

scoreboard = Scoreboard()

ball = Ball()

screen.bgcolor("black")
screen.update()

screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

screen.listen()

playing = True
while playing:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.flipy()
    elif -340 < ball.xcor() < -320 and ball.distance(l_paddle) < 50 or 340 > ball.xcor() > 320 and \
            ball.distance(r_paddle) < 50:
        print("Hit paddle")
        ball.flipx()
    elif ball.xcor() >= 380:
        ball.reset()
        scoreboard.left_scored()
        scoreboard.update()
    elif ball.xcor() <= -380:
        ball.reset()
        scoreboard.right_scored()
        scoreboard.update()

screen.exitonclick()
