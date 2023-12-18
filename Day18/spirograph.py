import random
import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
t.colormode(255)


def random_color():
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)
    color = (R, G, B)
    return color


timmy_the_turtle.speed("fastest")


def draw_spirograph(size):
    for x in range(int(360 / size)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + 10)


draw_spirograph(10)
