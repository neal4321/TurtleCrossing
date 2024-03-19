from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()

    def mark_score(self, level):
        self.goto(-220, 260)
        self.clear()
        self.write("{}".format(f"Level: {level}"), align="center", font=FONT)

    def game_over(self):
        self.write("{}".format(f"GAME OVER"), align="center", font=FONT)
