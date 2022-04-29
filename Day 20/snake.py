from turtle import Turtle
import time


class Snake:
    def __init__(self):
        self.snakes = []
        last_location = 0
        for i in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.up()
            new_turtle.goto(last_location, 0)
            self.snakes.append(new_turtle)
            last_location = new_turtle.xcor() - 20

    def move(self):
        for squares in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[squares - 1].xcor()
            new_y = self.snakes[squares - 1].ycor()
            self.snakes[squares].goto(new_x, new_y)

        self.snakes[0].forward(20)

    def up(self):
        self.snakes[0].setheading(90)

    def down(self):
        self.snakes[0].setheading(270)

    def left(self):
        self.snakes[0].setheading(180)

    def right(self):
        self.snakes[0].setheading(0)


    #     self.create_snake()
    #
    # def create_snake(self):
    #     for i in range(0, 3):
    #         body = Turtle(shape="square")
    #         body.up()
    #         body.color("white")
    #         body.setx(snake_position[i])
    #         body.goto(snake_position[i], 0)
    #         snake_body.append(body)
    #         snake_position.append(body.xcor() - 20)
    #
    # def move(self):
    #     for squares in range(len(snake_body) - 1, 0, -1):
    #         print(squares)
    #         new_x = snake_body[squares - 1].xcor()
    #         new_y = snake_body[squares - 1].ycor()
    #         snake_body[squares].goto(new_x, new_y)
    #     snake_body[0].forward(20)
