from turtle import Turtle, Screen

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(height=400, width=500)

user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

x_cords = -230
y_cords = -100

for i in range(5):
    new_turtle = Turtle()
    turtles.append(new_turtle)
    turtles[i].up()
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].goto(x=x_cords, y=y_cords)
    y_cords = y_cords + 40

racing = True
while racing:



screen.exitonclick()
