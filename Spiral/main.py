import turtle

turtle_object = turtle.Turtle()
screen_object = turtle.Screen()

screen_object.bgcolor("black")
turtle_object.pencolor("red")

a= 0
b= 0
turtle_object.speed(0) #maximum speed
turtle_object.penup()
turtle_object.goto(0, 200)
turtle_object.pendown()

while True:
    turtle_object.forward(a)
    turtle_object.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    turtle_object.hideturtle()

turtle.done()