from turtle import Turtle

FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0

        with open("/root/Documents/PycharmProjects/snake_game/data.txt", mode="r") as score:
            highscore = score.read()

        self.highscore = int(highscore)
        self.color("white")
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score()

    def increase(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()
