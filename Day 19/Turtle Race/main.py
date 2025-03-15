import random
import turtle
from turtle import Turtle



screen = turtle.Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
screen.setup(width= 500,height=400)
colors = ['red', 'orange', 'yellow','green', 'blue', 'purple']

is_race_on = False

for turtle_index in range(6):
    tim = Turtle('turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y = -100 + (30 * turtle_index))

if user_bet:
    is_race_on = True



screen.exitonclick()