from turtle import Turtle, Screen
import random

Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.speed(0)

for _ in range(0,10):
    Leonardo.forward(10)
    Leonardo.penup()
    Leonardo.forward(10)
    Leonardo.pendown()

screen = Screen()
screen.exitonclick()

