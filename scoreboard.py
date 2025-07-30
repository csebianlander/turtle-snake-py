from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

with open("data.txt", "r") as data:
    contents = data.read()
    if contents:
        high_score = int(contents)
    else:
        high_score = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over. \n'R' to retry, click to exit.", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            print(self.high_score)
            with open("data.txt","w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()