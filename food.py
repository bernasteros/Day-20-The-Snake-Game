from turtle import Turtle
from random import randint


# The Food-class should inherit the properties of the Turtle-class
# Apart from Turtle in the parentheses, we have to add a super().__init__() after initialisation.


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")

        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

        # TODO Create Food as collision object on the road
    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)