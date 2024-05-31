import turtle


class Projectile(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("light green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.setheading(90)

    def move(self):
        y = self.ycor()
        y += 20
        self.sety(y)