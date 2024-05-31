import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-320, 375)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))

    def increase_score(self, points):
        self.score += points
        self.update_scoreboard()