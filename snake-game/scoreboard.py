from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update_score()


    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        with open("data.txt",mode="w") as data:
            data.write(str(self.highscore))
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.highscore}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()
