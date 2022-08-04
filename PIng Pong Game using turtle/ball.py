from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.07
        
    def Move(self):
        go_x = self.xcor() + self.move_x
        go_y = self.ycor() + self.move_y
        self.goto(go_x, go_y)

    def Bounce_y(self):
        self.move_y *= -1

    def Bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def resetPosition(self):
        self.home()
        self.move_speed = 0.07
        self.Bounce_x()
