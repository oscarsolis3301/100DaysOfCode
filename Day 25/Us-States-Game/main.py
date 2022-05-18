from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.setup(width=725, height=491)
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

states_file = pandas.read_csv("50_states.csv")
states = states_file.state.to_list()

amount_correct = 0
correct_guesses = []
playing = True
while playing:
    user_guess = screen.textinput(prompt="What's another state name?", title=f"{amount_correct}/50 States Correct")
    if user_guess.lower() == "exit":
        break
    for i in states:
        if user_guess.title() == i and user_guess.title() not in correct_guesses:
            amount_correct += 1
            correct_guesses.append(user_guess.title())
            user_state = states_file[states_file["state"] == user_guess.title()]
            state = Turtle()
            location = (user_state["x"].item(), user_state["y"].item())
            state.ht()
            state.up()
            state.goto(location)
            state.write(user_guess.title())
        elif user_guess.title() in correct_guesses:
            pass

did_not_guess = ["States Not Guessed"]
for state in states:
    if state not in correct_guesses:
        did_not_guess.append(state)

print(did_not_guess)

db = pandas.Series(did_not_guess)
db.to_csv("States_to_Study.csv", index=False, header=False)

