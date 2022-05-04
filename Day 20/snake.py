from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes = []
        self.last_location = 0
        self.start()
        self.head = self.snakes[-1]

    def start(self):
        for i in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.speed("fastest")
            new_turtle.color("white")
            new_turtle.up()
            self.snakes.append(new_turtle)
            self.new_turtle_locations(new_turtle)

    def new_turtle_locations(self, turtle):
        turtle.goto(self.last_location, 0)
        self.last_location = turtle.xcor() - 20

    def create(self):
        new_turtle = Turtle(shape="square")
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.up()
        new_turtle.goto(self.snakes[0].xcor(), self.snakes[0].ycor())
        self.snakes.append(new_turtle)

    def extend(self):
        self.create()

    def move(self):
        for squares in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[squares - 1].xcor()
            new_y = self.snakes[squares - 1].ycor()
            self.snakes[squares].goto(new_x, new_y)

        self.snakes[0].forward(20)

    def up(self):
        if self.snakes[0].heading() == DOWN:
            pass
        else:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() == UP:
            pass
        else:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() == RIGHT:
            pass
        else:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() == LEFT:
            pass
        else:
            self.snakes[0].setheading(RIGHT)

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
