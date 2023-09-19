import turtle
from turtle import Turtle, Screen
import random

race_starts = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title = "Make your bet", prompt ="Which turtle do you think will win the race. Insert a colour:")
colours = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-100, -70, -40, -10, 20, 50]
racing_turtle = []

for turtles in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtles])
    new_turtle.goto(x = -220, y = y_positions[turtles])
    racing_turtle.append(new_turtle)

if bet:
    race_current = True

while race_current:
    for turtle in racing_turtle:
        if turtle.xcor() >230:
            race_current = False
            winning_colour = turtle.pencolor()
            if winning_colour == bet:
                print(f"You have won. The {winning_colour} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_colour} turtle was the winner.")
        rand_distance = random.randint(0,20)
        turtle.forward(rand_distance)


screen.exitonclick()