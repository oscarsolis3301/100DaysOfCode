from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
snake_body = []
snake_position = [0]
screen.tracer(0)

for i in range(0, 3):
    body = Turtle(shape="square")
    body.up()
    body.color("white")
    body.setx(snake_position[i])
    body.goto(snake_position[i], 0)
    snake_body.append(body)
    snake_position.append(body.xcor() - 20)

running = True
while running:
    screen.update()
    time.sleep(.1)
    for squares in range(len(snake_body) - 1, 0, -1):
        print(squares)
        new_x = snake_body[squares - 1].xcor()
        new_y = snake_body[squares - 1].ycor()
        snake_body[squares].goto(new_x, new_y)
    snake_body[0].forward(20)

#
# def move_right():
#
#     x_before = snake_body[0].xcor()
#     snake_body[0].right(90)
#     snake_body[0].forward(20)
#     x_after = snake_body[0].xcor()
#
#     for x in range(1, len(snake_body)):
#         snake_body[x].setx(x_before)
#
#
# def move_forward():
#     for squares in snake_body:
#         squares.forward(10)
#
#
# def move_left():
#     snake_body[0].left(90)
#     snake_body[0].forward(10)
#     for squares in snake_body:
#         squares.forward(10)
#
#
# def move_down():
#     for squares in snake_body:
#         squares.forward(10)
#
#
# screen.listen()
# screen.onkey(move_right, "Right")
# screen.onkey(move_left, "Left")
# screen.onkey(move_forward, "Up")
# screen.onkey(move_down, "Down")
screen.exitonclick()
