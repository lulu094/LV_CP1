# LV 2nd Maze Generator
# Creates a 6x6 maze 

import turtle
import random

# Set up the drawing canvas and turtle
def setup_turtle():
    turtle.setup(width=600, height=600)  # Make the window square
    turtle.speed(0)                      # Draw as fast as possible
    turtle.hideturtle()                  # Hide the turtle icon
    turtle.penup()
    turtle.goto(-250, 250)               # Start at top-left corner
    turtle.pendown()
    turtle.pensize(2)                    # Thicker lines for better visibility

# Draw a single cell with random wall openings
def draw_cell(x, y, cell_size):
    # Figure out where to start drawing this cell
    start_x = -250 + x * cell_size
    start_y = 250 - y * cell_size

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.setheading(0)  # Face right
    turtle.pendown()

    # Draw the four sides of the cell
    for _ in range(4):
        if random.choice([True, False]):
            turtle.forward(cell_size)  # Draw wall
        else:
            turtle.penup()
            turtle.forward(cell_size)  # Leave gap
            turtle.pendown()
        turtle.right(90)  # Turn to draw next side

# Build the full maze grid
def generate_maze(rows, cols, cell_size):
    for y in range(rows):
        for x in range(cols):
            draw_cell(x, y, cell_size)

# Mark the start and end points of the maze
def mark_points(rows, cols, cell_size):
    turtle.penup()

    # Start point (top-left)
    turtle.color("green")
    turtle.goto(-250 + cell_size / 3, 250 - cell_size / 1.5)
    turtle.write("START")

    # End point (bottom-right)
    turtle.color("red")
    turtle.goto(-250 + (cols - 1) * cell_size + cell_size / 3,
                250 - (rows - 1) * cell_size - cell_size / 1.5)
    turtle.write("END")

    turtle.color("black")  # Reset color for future drawing

# Check if the maze is solvable 
def is_solvable(row_grid, col_grid):
    size = len(row_grid)
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop()
        if x == size - 1 and y == -1:
            return True

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[x][x + 1] == "":
            stack.append((x + 1, y))
        if y < size - 1 and row_grid[y + 1][x] == "":
            stack.append((x, y + 1))
        if x > 0 and col_grid[y][x] == "":
            stack.append((x - 1, y))
        if y > 0 and row_grid[y][x] == "":
            stack.append((x, y - 1))

