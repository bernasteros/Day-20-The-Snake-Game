import time
from turtle import Screen, Turtle
from snake import Snake
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# TODO Create a initial Snake with square-turtles

snake = Snake()

# TODO Move the Snake

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


# TODO Steer the Snake
# TODO Create Food as collision object on the road
# TODO Expand the Snake if it collides with food
# TODO Scoreboard
# TODO Game-Over Conditions



screen.exitonclick()