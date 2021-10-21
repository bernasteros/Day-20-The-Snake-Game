from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create a initial Snake with square-turtles
square_list = []
for initial_square in range(0, 3):
    new_square = Turtle()
    new_square.shape("square")
    new_square.color("white")
    new_square.penup()
    new_square.setx(0 - 20*initial_square)

# TODO Move the Snake
# TODO Steer the Snake
# TODO Create Food as collision object on the road
# TODO Expand the Snake if it collides with food
# TODO Scoreboard
# TODO Game-Over Conditions



screen.exitonclick()