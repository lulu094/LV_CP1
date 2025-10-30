# LV - CS1400A - Turtle Race

# This program creates a turtle race using the turtle and random libraries.
# Five turtles of different colors race to a clearly marked finish line.
# The winner is announced in the terminal once one crosses the finish line.

import turtle  # built-in library to draw and create turtles
import random  # built-in library to generate random numbers

pink = "#DDA0DD"
brown = "#A52A2A"
violet = "#CF9FFF"
green = "#E4D00A"
orange = "#FFA500"
# Create screen, draw finish line, and position turtles for the race.

def setup_race():
    """Set up the race screen, draw finish line, and place turtles."""
    
    # Create and configure the drawing screen
    screen = turtle.Screen()
    screen.title("LV 2nd Turtle Race")

    # Draw the finish line
    line = turtle.Turtle()
    line.hideturtle()
    line.pensize(5)
    line.penup()
    line.goto(200,300)
    line.right(90)
    line.pendown()
    line.forward(300)

    # Create five turtles with unique colors
    colors = ["brown", "orange", "pink", "violet", "green"]
    start_y = 250
    turtles = []

    for color in colors:
        racer = turtle.Turtle()
        racer.shapesize(2)
        racer.shape("turtle")
        racer.pensize(5)
        racer.color(color)
        racer.penup()
        racer.goto(-600, start_y)
        racer.pendown()
        turtles.append(racer)
        start_y -= 50  # move each turtle down a bit

    return turtles



# Move turtles forward by random steps until one crosses the finish line.

def race_turtles(turtles):
    """Make turtles race by moving random steps each round."""
    race_on = True
    winner = None

    while race_on:
        for racer in turtles:
            # Move each turtle forward a random number of pixels
            distance = random.randint(1, 10)
            racer.forward(distance)

            # Check for winner
            if racer.xcor() >= 200:
                winner = racer.pencolor()
                race_on = False
                break

    return winner


# Display winner message and stop the program.

def announce_winner(winner_color):
    """Announce the winner of the race."""
    print(f"The {winner_color} turtle won!")  # print to terminal

    # Display message on screen
    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(-50, 0)
    announcer.write(f"The {winner_color} turtle won!", font=("Arial", 16, "bold"))

    turtle.done()

# 1. Setup race screen and turtles
# 2. Start race
# 3. Announce winner

def main():
    turtles = setup_race()
    winner_color = race_turtles(turtles)
    announce_winner(winner_color)


# Run the program
if __name__ == "__main__":
    main()
