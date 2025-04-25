import turtle

import pandas
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv',sep=',')
guessed_states = []
all_states = data['state'].to_list()
missing_states = []
while len(guessed_states)<50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in data['state'].to_list():
        guessed_states.append(answer_state)
        state_data = data[data['state']==answer_state]
        x_cor = state_data['x'].item()
        y_cor = state_data['y'].item()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_cor),int(y_cor))
        t.write(answer_state)
screen.exitonclick()
