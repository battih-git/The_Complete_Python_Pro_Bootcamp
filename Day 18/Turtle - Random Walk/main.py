import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

turtle.colormode(255)
directions = [0,90,180,270]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

for _ in range(200):
    tim.pensize(15)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.speed(50)




screen = Screen()
screen.exitonclick()