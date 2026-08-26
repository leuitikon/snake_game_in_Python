from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())


        self.speed(0)
        self.hideturtle()



    def increase_score(self):
        self.score += 1
        self.score_board()


    def score_board(self):
        self.color("white")
        self.penup()
        self.goto(0,269)
        self.write(f"Score = {self.score} High score: {self.high_score}", False, align="center", font=("Courier", 24, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.score_board()
