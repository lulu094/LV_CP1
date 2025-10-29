# LV 2nd Turtle Race

# Import libraries
import turtle
import random


# Draw the end line
turtle.pensize(5)
turtle.shapesize(0.2)
turtle.shape("circle")
turtle.penup()
turtle.goto(200,300)
turtle.right(90)
turtle.pendown()
turtle.forward(500)
turtle.end_fill()
turtle.done()
# Setting the turtles :colors shape and placement
purple = turtle.Turtle()
purple.color("#E6E6FA")
purple.shape("turtle")
purple.goto(-100,250)
purple.forward()
purple.speed(random)
turtle.done()

red = turtle.Turtle()
red.color("#800020")
red.goto(-100,200)
red.shape("turtle")

blue = turtle.Turtle()
blue.color("#00FFFF")
blue.goto(-100,150)
blue.shape("turtle")

green = turtle.Turtle()
green.color("#BAB86C")
green.goto(-100,100)
green.shape("turtle")

yellow = turtle.Turtle()
yellow.color("#FDDA0D")
yellow.goto(-1,50)

for x in range:
    #800020