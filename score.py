from os import remove as rm
from turtle import Turtle

STYLE = ('Courier', 20, 'bold')
with open("data.txt", mode="r") as file:
    HIGH_SCORE = file.read()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(250)
        self.color("white")
        self.penup()
        self.count = 0
        self.write("Current Score:" + str(self.count) + "       High Score:"
                   + HIGH_SCORE, font=STYLE, align='center')

    def count_up(self):
        self.count += 1
        self.clear()
        self.write("Score:" + str(self.count), font=STYLE, align='center')

    def game_over(self):
        self.clear()
        self.color("red")
        self.sety(0)
        self.write("Game Over!\n Final Score:" + str(self.count), font=STYLE, align='center')

        if self.count > int(HIGH_SCORE):
            rm("data.txt")
            with open("data.txt", mode="w") as new_high_score:
                new_high_score.write(str(self.count))
