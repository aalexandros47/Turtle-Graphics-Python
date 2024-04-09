# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('DotArt.jpg', 36)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen
import random

# Define a list of color tuples
color_list = [(1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165), (70, 70, 45), (185, 190, 201), (126, 225, 231), (88, 49, 45), (61, 65, 66)]

# Create the turtle object
turtle_object = Turtle()
turtle_object.speed(0)
turtle_object.penup()
turtle_object.hideturtle()
# Create the screen object and set its colormode to 255 for RGB
screen = Screen()
screen.colormode(255)

#bring the turtle to this position
turtle_object.setheading(255)
turtle_object.forward(300)
turtle_object.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    # Draw a dot with a random color from the color_list
    turtle_object.dot(20, random.choice(color_list))
    turtle_object.forward(50)

    # 10,20,30,40,50,60,70,80,90,100 - changes direction
    if dot_count % 10 == 0:
        turtle_object.setheading(90)
        turtle_object.forward(50)
        turtle_object.setheading(180)
        turtle_object.forward(500)
        turtle_object.setheading(0)

# Wait for a user click to exit
screen.exitonclick()
