from turtle import Turtle, Screen

Leonardo = Turtle()
Leonardo.shape("turtle")
Leonardo.color("green")

for _ in range(0,4):
    #Square
    Leonardo.forward(100)
    Leonardo.right(90)

screen = Screen()
screen.exitonclick()

'''
    #Square range(0,4)
    Leonardo.forward(100)
    Leonardo.right(90)
'''

'''
    #Triangle range(0,3)
    Leonardo.forward(100)
    Leonardo.right(120)
'''