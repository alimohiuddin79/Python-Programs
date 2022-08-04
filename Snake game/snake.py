from turtle import Turtle, Screen
import turtle
STARTING_POS = [(0, 0), (0, -20), (0, -40)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_turtle(position)

    def add_turtle(self, position):
        new_turtle = Turtle("square");
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_body.append(new_turtle)

    def extend(self):
        self.add_turtle(self.snake_body[-1].position())

    def move(self):
        for state in range(len(self.snake_body) - 1, 0, -1):
            new_state_x = self.snake_body[state - 1].xcor()
            new_state_y = self.snake_body[state - 1].ycor()
            self.snake_body[state].goto(new_state_x, new_state_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
