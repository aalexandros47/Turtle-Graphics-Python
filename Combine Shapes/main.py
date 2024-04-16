from turtle import Turtle, Screen
import random

Leonardo = Turtle()
Leonardo.shape("turtle")
colours =["MediumVioletRed","DarkGreen","Blue","Indigo","Red","Lime",]
Leonardo.speed(0)

def draw_shape(number_of_sides):
    angle = 360 / number_of_sides

    for _ in range(number_of_sides):
        Leonardo.forward(100)
        Leonardo.right(angle)

for n_of_sides in range(3,11):
    Leonardo.color(random.choice(colours))
    draw_shape(n_of_sides)

screen = Screen()
screen.exitonclick()

