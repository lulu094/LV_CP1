# LV 2nd Maze Generator
# A simple 6x6 maze generator using turtle, nested loops, and conditionals

import turtle
import random

# Functions

def setup_turtle():
    """
    Sets up the turtle window and pen.
    - Makes the drawing area a square.
    - Moves the turtle to the top-left corner.
    - Hides the turtle and makes it draw faster.
    """
    turtle.setup(width=600, height=600)
    turtle.speed(0)          # Fastest drawing
    turtle.hideturtle()      # Hide turtle icon
    turtle.penup()           # Don't draw while moving
    turtle.goto(-250, 250)   # Start in top-left corner
    turtle.pendown()         # Start drawing again
    turtle.pensize(2)        # Thicker lines for walls


# Drawing function

def draw_cell(x, y, cell_size):
    """
    Draw one cell of the maze grid.
    Each cell is a square, but we randomly skip one wall
    so that there are openings between some cells.
    """
    # Move turtle to correct spot based on row and column
    start_x = -250 + x * cell_size
    start_y = 250 - y * cell_size

    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.setheading(0)   # Face right
    turtle.pendown()

    # --- Pseudocode for drawing walls ---
    # For each side of the square:
    #   - Sometimes draw the wall
    #   - Sometimes skip it to make an opening
    for side in range(4):
        # Conditional: randomly decide if wall is drawn or skipped
        draw_wall = random.choice([True, False])

        if draw_wall:
            turtle.forward(cell_size)  # Draw a wall
        else:
            turtle.penup()             # Skip a wall
            turtle.forward(cell_size)
            turtle.pendown()
        turtle.right(90)  # Turn 90 degrees for the next side


# MAZE GENERATION FUNCTION

def generate_maze(rows, cols, cell_size):
    """
    Uses nested loops to draw the maze grid.
    Outer loop goes through each row.
    Inner loop goes through each column.
    """
    for y in range(rows):          # Loop over rows (top to bottom)
        for x in range(cols):      # Loop over columns (left to right)
            # Call the draw_cell function to draw each square
            draw_cell(x, y, cell_size)

# MARK START & END

def mark_points(rows, cols, cell_size):
    """
    Marks the start (top-left) and end (bottom-right) of the maze.
    """
    turtle.penup()

    # --- Start ---
    turtle.color("green")
    turtle.goto(-250 + cell_size / 3, 250 - cell_size / 1.5)
    turtle.write("START", font=("Arial", 10, "bold"))

    # --- End ---
    turtle.color("red")
    turtle.goto(-250 + (cols - 1) * cell_size + cell_size / 3,
                250 - (rows - 1) * cell_size - cell_size / 1.5)
    turtle.write("END", font=("Arial", 10, "bold"))

    turtle.color("black")  # Reset color

def is_solvable(row_grid, col_grid):
    size = len(row_grid)
    visited = set()
    stack=[(0,0)]

    while stack:
        x,y = stack.pop()
        if x == size - 1 and y == -1:
            return True
        
        if (x,y) in visited:
            continue

        visited.add((x,y))
        if x < size - 1 and col_grid[x][x+1] == "":
            stack.append((x+1,y))

        if y < size - 1 and row_grid[y+1][x] == "":
            stack.append((x, y+1))

        if x > 0 and col_grid[y][x] == "":
            stack.append((x-1,y))

        if y > 0 and row_grid[y][x] == "":
            stack.append((x, y-1))

# MAIN FUNCTION

def main():
    """
    Main function to run the maze program.
    - Sets up the screen.
    - Defines maze size.
    - Generates the maze.
    - Marks start and end points.
    """
    setup_turtle()

    # Maze size
    rows = 6
    cols = 6
    cell_size = 60

    # Generate the maze
    generate_maze(rows, cols, cell_size)

    # Mark the start and end
    mark_points(rows, cols, cell_size)

    # Keep window open until user closes it
    turtle.done()


# RUN PROGRAM

if __name__ == "__main__":
    main()




