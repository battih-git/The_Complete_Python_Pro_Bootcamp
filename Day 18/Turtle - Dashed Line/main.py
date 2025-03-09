# import module
import random
from turtle import Turtle, Screen
import heroes #installation of new module

# creating object tim
tim = Turtle()


# Draw a dashed line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()