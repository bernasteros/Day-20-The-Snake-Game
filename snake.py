from turtle import Turtle

# Constant convention: BIG_LETTERS_ONLY
# Helps to change things fast, without searching the code

# Overall Properties
MOVE_DISTANCE = 20
COLOR = "white"
SHAPE = "square"
SNAKE_LENGTH = 3

# Steering
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
        for initial_square in range(SNAKE_LENGTH):
            start_square = Turtle()
            start_square.shape(SHAPE)
            start_square.color(COLOR)
            start_square.penup()
            start_square.setx(0 - 20 * initial_square)
            self.body.append(start_square)

    def add_part(self):

        additional_square = Turtle()
        additional_square.shape(SHAPE)
        additional_square.color(COLOR)
        additional_square.penup()

        last_square_location = self.body[-1].position()

        additional_square.setposition(last_square_location)
#        last_square_heading = self.body[-1].heading()
#        last_x = int(last_square_location[0])
#        last_y = int(last_square_location[1])
#
#        if last_square_heading == DOWN:
#            additional_square.setposition(last_x, last_y + 20)
#
#        elif last_square_heading == UP:
#            additional_square.setposition(last_x, last_y - 20)
#
#        elif last_square_heading == RIGHT:
#            additional_square.setposition(last_x - 20, last_y)
#
#        elif last_square_heading == LEFT:
#            additional_square.setposition(last_x + 20, last_y)
        self.body.append(additional_square)

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