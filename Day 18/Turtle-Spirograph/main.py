import random
import turtle
from turtle import Turtle

tim = Turtle()
tim.speed('fastest')


turtle.colormode(255)
def random_color():
    "Returns a tuple of random r,g,b color code in range 0-255"
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)



screen = turtle.Screen()
screen.exitonclick()