# LV 2nd Maze Generator
import turtle
import random


# Maze Configuration

rows = 6
cols = 6
cell_size = 50

# Maze grid: each cell has 4 walls (top, right, bottom, left)
maze = [[[True, True, True, True] for c in range(cols)] for r in range(rows)]

# Visited grid for maze generation
visited = [[False] * cols for _ in range(rows)]


# Turtle Setup

def setup_turtle():
    turtle.setup(600, 600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-250, 250)
    turtle.pendown()


# Maze Generation
# wall removal

def walls(x, y):
    visited[y][x] = True
    # Up, Right, Down, Left (dx, dy, wall_index)
    directions = [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]
    random.shuffle(directions)
    # dy change in y
    # dx change in x
    for dx, dy, wall_index in directions:
        nx, ny = x + dx, y + dy
        # Check boundaries and if not visited
        if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx]:
            # Remove wall between current and next cell
            maze[y][x][wall_index] = False
            maze[ny][nx][(wall_index + 2) % 4] = False
            walls(nx, ny)  # Recursive call
            # nx next x
            # ny next

# Draw One Cell

def draw_cell(x, y):
    start_x = -250 + x * cell_size
    start_y = 250 - y * cell_size
    turtle.penup()
    turtle.goto(start_x, start_y)
    
    # Each wall: top, right, bottom, left
    for i, (dx, dy) in enumerate([(cell_size, 0), (0, -cell_size), (-cell_size, 0), (0, cell_size)]):
        if maze[y][x][i]:  # Conditional for wall existence
            turtle.pendown()
        else:
            turtle.penup()
        turtle.goto(turtle.xcor() + dx, turtle.ycor() + dy)

    turtle.penup()


# Draw the Entire Maze
def draw_maze():
    setup_turtle()
    walls(0, 0)  # Generate maze recursively
    
    # Nested loops to draw each cell
    for row in range(rows):
        for col in range(cols):
            draw_cell(col, row)

    # Mark start (green) and end (red)
    turtle.penup()
    turtle.goto(-225, 225)
    turtle.dot(15, "green")  # Start
    turtle.goto(-250 + (cols - 1) * cell_size + 25, 250 - (rows - 1) * cell_size - 25)
    turtle.dot(15, "red")    # End

    print("Maze done!")


# Run Program

draw_maze()
turtle.done()
