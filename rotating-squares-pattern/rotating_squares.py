import turtle

turtle_object = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
turtle_object.pencolor("white")
turtle_object.speed(0)
x = 0
y = 0
while True:
    for i in range(4):
        turtle_object.forward(80)
        turtle_object.right(90)
    turtle_object.right(5)
    x += 1
    if x>= 390/5:
        turtle_object.forward(50)
        x = 0
        y += 1
        if y>= 12:
            break
turtle_object.hideturtle()
turtle.done()
