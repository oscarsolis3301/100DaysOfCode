from turtle import Turtle, Screen

timmy = Turtle()


def draw():
    sides = 3
    while sides != 11:
        angel = 360 / sides
        for _ in range(sides):
            timmy.forward(100)
            timmy.right(angel)

        sides += 1


# Continues to draw all shapes until finished
draw()

screen = Screen()
screen.exitonclick()
