import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
scoreboard = Scoreboard()

# Listening to the keys of the user; Turtle can only go up
screen.listen()
screen.onkeypress(user.move, "Up")

cars = []
speed = .1
playing = True
car_amount = 10


def game_over():
    print("GAME OVER")
    scoreboard.game_over()
    screen.exitonclick()
    return False


# Main game loop
while playing:
    time.sleep(speed)
    screen.update()
    # Starts the first few cars
    if 0 <= len(cars) < car_amount:
        for i in range(10):
            car = CarManager()
            cars.append(car)

    for x in range(len(cars)):
        cars[x].move()
        if user.distance(cars[x]) <= 35:
            playing = game_over()

        if cars[x].xcor() <= -350:
            cars.remove(cars[x])
            car = CarManager()
            cars.append(car)

    if user.ycor() == 280:
        user.home()
        scoreboard.level_up()
        speed -= (speed / 1.2)
        car_amount += (car_amount / 2)
