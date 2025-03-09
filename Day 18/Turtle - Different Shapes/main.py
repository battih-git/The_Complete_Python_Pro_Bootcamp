# import module
import random
from turtle import Turtle, Screen
import heroes #installation of new module

# creating object tim
tim = Turtle()


colors = ['cornflower blue', 'dodger blue', 'pale goldenrod', 'dark salmon', 'wheat' ]


# Function to draw a shape
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)



for shape_side in range(3,11):
    tim.pencolor(random.choice(colors))
    draw_shape(shape_side)


screen = Screen()
screen.exitonclick()