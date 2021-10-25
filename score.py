from turtle import Turtle

STYLE = ('Courier', 30, 'bold')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.sety(250)
        self.color("white")
        self.penup()
        self.count = 0
        self.write("Score:" + str(self.count), font=STYLE, align='center')

    def count_up(self):
        self.count += 1
        self.clear()
        self.write("Score:" + str(self.count), font=STYLE, align='center')

    def game_over(self):
        self.clear()
        self.color("red")
        self.sety(0)
        self.write("Game Over!\n Final Score:" + str(self.count), font=STYLE, align='center')
