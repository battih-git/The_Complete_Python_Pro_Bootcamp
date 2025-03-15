import random
import turtle
from turtle import Turtle

import colorgram

# colors = colorgram.extract('sample.jpeg',30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

color_code = [(245, 242, 243), (179, 11, 33), (183, 172, 13), (187, 74, 23), (248, 214, 73), (212, 157, 76), (171, 23, 16), (114, 185, 204),
              (50, 96, 159), (61, 48, 109), (224, 128, 160), (203, 234, 223), (67, 35, 61), (35, 54, 70), (39, 136, 85), (249, 57, 21),
              (165, 48, 72), (100, 187, 158), (222, 70, 137), (230, 237, 244), (77, 46, 37), (245, 199, 1), (149, 211, 223), (52, 173, 190),
              (16, 168, 152), (157, 183, 229), (80, 104, 180), (44, 59, 59), (88, 73, 35)]
turtle.colormode(255)

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed('fastest')
num_of_dots = 100

for dot_count in range(1,num_of_dots+1):
    color = random.choice(color_code)
    tim.dot(20,color)
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle.Screen()
screen.exitonclick()