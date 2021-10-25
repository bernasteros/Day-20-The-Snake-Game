from turtle import Screen
from snake import Snake
from food import Food
from time import sleep
from score import Score

border = (300, 300)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create a initial Snake with square-turtles (moved into class)

snake = Snake()
food = Food()
score = Score()

# Move the Snake

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # collision with food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_part()
        score.count_up()

    # TODO implement collision detection with own body

    if -300 < int(snake.head.position()[0]) < 300 and -300 < int(snake.head.position()[1]) < 300:
        continue
    else:
        game_is_on = False

snake.reset()
score.game_over()



screen.exitonclick()