import random

import colorgram
import turtle as turtle_module

colors = colorgram.extract("image.jpg", 10)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle = turtle_module.Turtle()
turtle_module.colormode(255)

turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)


def draw_line():
    for x in range(10):
        turtle.dot(20, random.choice(rgb_colors))
        turtle.penup()
        turtle.forward(40)

    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(400)
    turtle.setheading(0)


for x in range(10):
    draw_line()

screen = turtle_module.Screen()
screen.exitonclick()
