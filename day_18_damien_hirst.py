# import colorgram
#
# rgb_colours = []
# colours = colorgram.extract('image.jpg', 20)
#
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)

# print(rgb_colours)

import turtle as t_module
import random

t_module.colormode(255)
timmy = t_module.Turtle()
timmy.hideturtle()

colour_list = [(234, 222, 113), (28, 109, 184), (225, 61, 90), (224, 151, 90), (124, 153, 205), (215, 130, 162), (139, 89, 52), (38, 194, 107), (105, 108, 190), (140, 177, 27), (240, 155, 184), (186, 48, 80), (109, 192, 156), (224, 63, 55), (186, 18, 37), (20, 182, 210)]

def turn_left():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(50)

def turn_right():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)
    timmy.forward(50)

def draw_10_dots():
    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, random.choice(colour_list))
        timmy.penup()
        timmy.forward(50)

timmy.penup()
timmy.setposition(-200,-200)



for _ in range(5):
    draw_10_dots()
    turn_left()
    draw_10_dots()
    turn_right()


screen = t_module.Screen()
screen.exitonclick()