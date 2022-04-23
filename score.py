
from turtle import Turtle

STYLE = ('Courier', 20, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(250)
        self.color("white")
        self.penup()
        self.count = 0

        with open("data.txt", mode="r") as file:
            high_score = file.read()
            self.write("Current Score:" + str(self.count) + "       High Score:"
                       + high_score, font=STYLE, align='center')

    def count_up(self):
        self.count += 1
        self.clear()
        self.write("Score:" + str(self.count), font=STYLE, align='center')

    def game_over(self):
        self.clear()
        self.color("red")
        self.sety(0)
        self.write("Game Over!\n Final Score:" + str(self.count), font=STYLE, align='center')

        # TODO: Find a way to replace the old data with the new one

        with open("data.txt", mode="r+") as file:
            high_score = file.read()
            if self.count > int(high_score):
                high_score.replace(str(self.count), high_score)
