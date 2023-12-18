import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    R = random.random()
    B = random.random()
    G = random.random()
    timmy_the_turtle.color(R, G, B)
    
    for x in range(0, number_of_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


draw_shape(4)
draw_shape(5)
draw_shape(6)
draw_shape(7)
draw_shape(8)
draw_shape(9)
draw_shape(10)
draw_shape(11)

screen = Screen()
screen.exitonclick()
