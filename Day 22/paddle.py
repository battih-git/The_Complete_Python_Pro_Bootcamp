from turtle import Turtle

from matplotlib.pyplot import xcorr


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(5, 1)
        self.color('white')
        self.penup()
        self.position = position
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)