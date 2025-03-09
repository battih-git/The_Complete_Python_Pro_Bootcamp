# import module
import random
from turtle import Turtle, Screen
import heroes #installation of new module

# creating object tim
tim = Turtle()
tim.shape("turtle")
tim.color("red")

# # Draw a simple square
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# heroes.gen()
#
# # Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw a triangle, square, pentagon, hexagon

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