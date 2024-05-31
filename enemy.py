import turtle
import random


class Enemy(turtle.Turtle):
    def __init__(self, shape, color, x, y):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.setheading(270)

    def move_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)


class EnemyProjectile(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.setheading(270)

    def move(self):
        y = self.ycor()
        y -= 20
        self.sety(y)