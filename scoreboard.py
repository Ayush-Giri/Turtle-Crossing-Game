from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-300, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(LEVEL_POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over_text(self):
        self.goto(0, 0)
        self.clear()
        self.write("Game Over", align="center", font=FONT)

    def increase_level(self):
        self.clear()
        self.goto(LEVEL_POSITION)
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)


