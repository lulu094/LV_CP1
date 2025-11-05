# LV 2nd Turtle Race
# This program makes 5 turtles race to a finish line!

import turtle
import random

# Set up the race 
def setup_race():
    # Make a screen
    screen = turtle.Screen()
    screen.title("LV 2nd Turtle Race")

    # Draw the finish line
    line = turtle.Turtle()
    line.hideturtle()
    line.pensize(5)
    line.penup()
    line.goto(200, 300)
    line.right(90)
    line.pendown()
    line.forward(300)

    # Make turtles
    colors = ["brown", "orange", "pink", "violet", "green"]
    turtles = []
    y = 250

    for color in colors:
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.penup()
        racer.goto(-600, y)
        racer.pendown()
        turtles.append(racer)
        y -= 50

    return turtles


# Make the turtles move
def race_turtles(turtles):
    race_on = True
    winner = None

    while race_on:
        for racer in turtles:
            step = random.randint(1, 10)
            racer.forward(step)

            # Check if a turtle reached the finish line
            if racer.xcor() >= 200:
                winner = racer.pencolor()
                race_on = False
                break

    return winner


# Show who won
def announce_winner(winner_color):
    print(f"The {winner_color} turtle won!")

    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(-50, 0)
    announcer.write(f"The {winner_color} turtle won!")

    turtle.done()


# Run the program
turtles = setup_race()
winner = race_turtles(turtles)
announce_winner(winner)
