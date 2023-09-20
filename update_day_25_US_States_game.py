import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

if len(guessed_states) < 50:
    game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    for state in states:
        if answer_state == state:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = data[data.state == f"{answer_state}"]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
        elif answer_state == "Exit":
            game_on = False
            missing_states = [state for state in states if state not in guessed_states ]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")

screen.exitonclick()
