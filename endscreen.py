import turtle


class EndScreen:
    def __init__(self, scoreboard):
        self.scoreboard = scoreboard

    def display_win(self, wn):
        wn.clear()
        wn.bgcolor("black")
        wn.title("You Win!")

        win_message = f"You Win!\nScore: {self.scoreboard.score}"
        win_text = turtle.Turtle()
        win_text.color("white")
        win_text.penup()
        win_text.hideturtle()
        win_text.goto(0, 0)
        win_text.write(win_message, align="center", font=("Arial", 24, "normal"))

    def display_lose(self, wn):
        wn.clear()
        wn.bgcolor("black")
        wn.title("You Lose!")

        lose_message = "You Lose!"
        lose_text = turtle.Turtle()
        lose_text.color("white")
        lose_text.penup()
        lose_text.hideturtle()
        lose_text.goto(0, 0)
        lose_text.write(lose_message, align="center", font=("Arial", 24, "normal"))