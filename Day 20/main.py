import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

screen.setup(width=600, height=600)
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        scoreboard.add_point()
