from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snakey Snack Attack")
screen.bgcolor("olivedrab")
screen.tracer(0)  # stops animation


def move_forward():
    snake.forward(10)


def move_backward():
    snake.backward(10)


def turn_left():
    snake.left(10)


def turn_right():
    snake.right(10)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # updates screen when all segments move forward
    time.sleep(0.1)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # detecting collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

# why these classes are important?
# if the snake doesn't work properly then we can understand that something wrong in the snake class
# and then we can refer back to this file and start making changes in the file.
