import random
import turtle
from turtle import Turtle



screen = turtle.Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
screen.setup(width= 500,height=400)
colors = ['red', 'orange', 'yellow','green', 'blue', 'purple']
all_turtles = []
is_race_on = False

for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y =-100 + (30 * turtle_index))
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    print(all_turtles)
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()