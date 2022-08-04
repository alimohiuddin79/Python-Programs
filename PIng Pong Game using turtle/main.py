import turtle
from turtle import Turtle, Screen
from divider import Divider
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

PLAYER_1_PADDLE = (350, 0)
PLAYER_2_PADDLE = (-350, 0)

screen = Screen()
screen.tracer(0)
screen.title("Ping Pong")
turtle.setup(width=800, height=600)
turtle.bgcolor("black")


# divider = Divider()
# divider.dividerLine()

r_paddle = Paddle(PLAYER_1_PADDLE)
l_paddle = Paddle(PLAYER_2_PADDLE)

ball = Ball()

scoreboard = Score()

screen.listen()
screen.onkeypress(r_paddle.go_Up, "Up")
screen.onkeypress(r_paddle.go_Down, "Down")
screen.onkeypress(l_paddle.go_Up, "w")
screen.onkeypress(l_paddle.go_Down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.Move()

    #Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.Bounce_y()

    #Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.Bounce_x()

    if ball.xcor() > 380:
        ball.resetPosition()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.r_point()

screen.exitonclick()
