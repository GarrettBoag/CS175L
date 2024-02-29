#Garrett Boag
#CS 175L 01
#STOP.py

import math
import turtle


# Named constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

turtle.hideturtle()
turtle.pensize(10)

turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.color("red")
turtle.pendown()

turtle.forward(s/2)

for x in range(1,8):
    turtle.right(45)
    turtle.forward(s)

turtle.right(45)
turtle.forward(s/2)

turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.pendown()

turtle.begin_fill()

turtle.forward(s/2 - 10)
for x in range(1,8):
    turtle.right(45)
    turtle.forward(s-20)

turtle.right(45)
turtle.forward(s/2 - 10)

turtle.end_fill()

turtle.penup()
turtle.forward(-80)
turtle.right(90)
turtle.forward(120)
turtle.left(90)
turtle.pencolor('Black')
turtle.write("STOP", font=("Cooper Black", 45, "normal"))



