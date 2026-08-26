from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Set up the game screen dimensions and background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard inputs to control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# Main game loop
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    # Allow the snake to accept new key directions after a frame update
    snake.reset_direction_lock()

    # Display the current score on the scoreboard
    scoreboard.score_board()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.reset()
        scoreboard.hideturtle()
        scoreboard.increase_score()

    # Detect collision with wall (fixed top/bottom boundaries to match 280)
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()