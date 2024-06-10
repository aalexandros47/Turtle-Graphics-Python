from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

WINNING_SCORE = 5

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0), "white")
l_paddle = Paddle((-350, 0), "white")
ball = Ball("white")
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect right paddle collision with the ball
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
        ball.increase_speed()

    # Detect left paddle collision with the ball
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.increase_speed()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        if scoreboard.l_score == WINNING_SCORE:
            scoreboard.game_over("Left Player Wins")
            game_is_on = False

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        if scoreboard.r_score == WINNING_SCORE:
            scoreboard.game_over("Right Player Wins")
            game_is_on = False

screen.exitonclick()
