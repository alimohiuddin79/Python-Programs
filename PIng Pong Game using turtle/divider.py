from turtle import Turtle, Screen


class Divider:
    def __init__(self):
        self.dividerLine()

    def dividerLine(self):
        divider = Turtle("square")
        divider.hideturtle()
        divider.penup()
        divider.pencolor("white")
        divider.pensize(10)
        divider.goto(0, -400)
        divider.setheading(90)
        for _ in range(18):
            divider.pendown()
            divider.forward(20)
            divider.penup()
            divider.forward(20)

