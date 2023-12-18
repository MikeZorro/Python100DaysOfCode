from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# for x in range(0, 4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

for a in range(16):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()








screen = Screen()
screen.exitonclick()