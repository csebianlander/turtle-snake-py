from turtle import Screen, Turtle

import snake
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SPEED = 0.1

# Screen set up


def start_game():
    screen = Screen()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("PySnake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(start_game, "r")

    game_over = False
    while not game_over:
        screen.update()
        time.sleep(SPEED)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            game_over = True
            scoreboard.game_over()

        # Detect collision with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_over = True
                scoreboard.game_over()

    screen.exitonclick()



start_game()