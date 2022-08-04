import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
turtle.setup(width=600, height=600)
turtle.title("Snake game")
turtle.bgcolor("black")
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_state = True

while game_state:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_state = False
        score.game_over()

    #Detect collision with snake tail.
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            game_state = False
            score.game_over()

screen.exitonclick()