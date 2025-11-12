# LV 2nd Maze Generator

# 1. Import turtle and random
# 2. Create a grid using simple loops (6x6)
# 3. Use nested loops to go through every square
# 4. Use if statements to decide when to draw walls
# 5. Use turtle to draw each cell and walls
# 6. Mark a start and end point in color

import turtle
import random


# - Set the window size
# - Set color, pensize, and speed
# - Move the turtle to top-left starting spot
def setup_turtle():
    turtle.setup(600, 600)
    turtle.color("#5D3FD3")  
    turtle.pensize(2)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-250, 250)
    turtle.pendown()


rows = 6
cols = 6
cell_size = 50

# build a simple 2D list (no fancy list comprehension)
maze = []
for row in range(rows):
    row_data = []
    for col in range(cols):
        # 1 means wall, 0 means open path
        row_data.append(1)
    maze.append(row_data)



# - Loop through every cell
# - Use random numbers to open up some paths
# - Use conditionals to control how many open cells appear
def make_maze():
    for r in range(rows):
        for c in range(cols):
            # random number 0 or 1
            number = random.randint(0, 1)

            # open up some random spaces
            if number == 0 or (r == 0 and c == 0):
                maze[r][c] = 0
            else:
                maze[r][c] = 1


# - Go to the top-left corner of that cell
# - Draw walls around it if the value is 1
# - If it’s 0, skip (no walls)
def draw_cell(col, row):
    start_x = -250 + col * cell_size
    start_y = 250 - row * cell_size
    turtle.penup()
    turtle.goto(start_x, start_y)

    # draw walls only if it's a wall cell
    if maze[row][col] == 1:
        turtle.pendown()
        for i in range(4):
            turtle.forward(cell_size)
            turtle.right(90)
    else:
        # leave it open to form paths
        pass
    turtle.penup()


# - Setup turtle
# - Call make_maze to fill grid
# - Use nested loops to draw all cells
# - Mark start and end points
def draw_maze():
    setup_turtle()
    make_maze()

    # draw each cell
    for r in range(rows):
        for c in range(cols):
            draw_cell(c, r)

    # Mark start and end with your original colors
    turtle.penup()
    turtle.goto(-225, 225)
    turtle.dot(15, "green")  # Start point
    turtle.goto(-225 + (cols - 1) * cell_size, 225 - (rows - 1) * cell_size)
    turtle.dot(15, "red")    # End point

    print("Maze created successfully!")


# run the program

draw_maze()
turtle.done()
