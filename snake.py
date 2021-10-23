from turtle import Turtle

# Constant convention: BIG_LETTERS_ONLY
# Helps to change things fast, without searching the code

MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.body = []
        self.new_body()

    def new_body(self):
        for initial_square in range(0, 3):
            new_square = Turtle()
            new_square.shape("square")
            new_square.color("white")
            new_square.penup()
            new_square.setx(0 - 20 * initial_square)
            self.body.append(new_square)

    def move(self):
        for tile_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[tile_num - 1].xcor()
            new_y = self.body[tile_num - 1].ycor()
            self.body[tile_num].goto(new_x, new_y)
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)