from turtle import Turtle

# Constant convention: BIG_LETTERS_ONLY
# Helps to change things fast, without searching the code

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.body = []
        self.new_body()
        self.head = self.body[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)