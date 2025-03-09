# import module
import random
from turtle import Turtle, Screen
import heroes #installation of new module

# creating object tim
tim = Turtle()


# Draw a simple square
for _ in range(4):
    tim.forward(100)
    tim.left(90)


screen = Screen()
screen.exitonclick()