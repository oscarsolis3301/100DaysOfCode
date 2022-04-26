from turtle import Turtle, Screen

tom = Turtle()


def move_backwards():
    tom.back(10)


def move_forward():
    tom.forward(10)


def rotate_left():
    tom.left(25)


def rotate_right():
    tom.right(25)


def clear_screen():
    tom.reset()


screen = Screen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=rotate_left)
screen.onkeypress(key="d", fun=rotate_right)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="c", fun=clear_screen)
screen.listen()

screen.exitonclick()
