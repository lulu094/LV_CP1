# LV 2nd Libraries Notes
import random
import turtle

number = random.randint(100,500)

gray=turtle.Turtle()# many turtles
f=turtle.Turtle()
#todd.forward(20)

turtle.shape("turtle")
turtle.shapesize(5)
turtle.color("#BAB86C")
turtle.pensize(5)
turtle.fillcolor("556B2F")
turtle.begin_fill()
for x in range(4): #making a square
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(50,6)#Where the turtle can go turtle starts at (0,0)
turtle.pendown()
turtle.begin_fill()
for x in range(4): #making a square
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.done()