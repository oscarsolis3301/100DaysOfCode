import time
from snake import Snake
from turtle import Screen

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")
snake = Snake()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


running = True
while running:
    screen.update()
    time.sleep(.1)
    snake.move()

