# LV 2nd Turtle Race 

# Import needed libraries
# Import turtle and random to use drawing and randomness
import turtle
import random

# Set up screen and race elements
def setup_race():
    # Create a window and draw the finish line
    screen = turtle.Screen()
    screen.title("Turtle Race")

    finish_line = turtle.Turtle()
    finish_line.hideturtle()
    finish_line.pensize(4)
    finish_line.penup()
    finish_line.goto(250, 200)
    finish_line.right(90)
    finish_line.pendown()
    finish_line.forward(400)

    # Create 5 turtles, each with a unique color and starting position
    colors = ["red", "blue", "green", "orange", "purple"]
    turtles = []
    start_y = 150

    for color in colors:
        racer = turtle.Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.goto(-250, start_y)
        start_y -= 60
        turtles.append(racer)

    return turtles

# Move turtles randomly until one wins
def race(turtles):
    #Repeat random movements until a turtle crosses finish line
    winner = None
    race_on = True

    while race_on:
        for t in turtles:
            step = random.randint(2, 10)
            t.forward(step)

            # (pseudocode) Check if any turtle has crossed the finish line
            if t.xcor() >= 250:
                winner = t.pencolor()
                race_on = False
                break

    return winner

# Announce the winner
def announce_winner(winner):
    # (pseudocode) Show which turtle won the race
    print("The winner is the", winner, "turtle!")  # print in terminal

    # Create a turtle to write the winner on the screen
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(-60, 0)
    writer.write("The " + winner + " turtle wins!", font=("Arial", 16, "bold"))

# Main function
def main():
    # (pseudocode) Set up race, start it, and show the winner
    racers = setup_race()
    winner_color = race(racers)
    announce_winner(winner_color)
    turtle.done()

# To run the program, just type:
# main()
