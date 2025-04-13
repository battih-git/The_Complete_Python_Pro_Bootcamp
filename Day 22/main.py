import time
from turtle import Turtle, Screen
from paddle import  Paddle
from ball import Ball
from scorecard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.screensize(800,600)
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800,height=600)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
Scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect wall collision
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor()>320 or ball.distance((l_paddle)) < 60 and ball.xcor() <-320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        Scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        Scoreboard.r_point()






screen.exitonclick()