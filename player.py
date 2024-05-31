import turtle
import time
from projectile import Projectile

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("light green")
        self.penup()
        self.speed(0)
        self.goto(0, -350)
        self.setheading(90)
        self.projectiles = []

    def fire_projectile(self):
        x = self.xcor()
        y = self.ycor() + 10
        projectile = Projectile(x, y)
        self.projectiles.append(projectile)



    def move_left(self):
        x = self.xcor()
        x -= 20
        if x < -380:
            x = -380
        self.setx(x)

    def move_right(self):
        x = self.xcor()
        x += 20
        if x > 380:
            x = 380
        self.setx(x)


