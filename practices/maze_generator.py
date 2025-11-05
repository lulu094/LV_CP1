# LV 2nd Maze Generator
# 1st set variables
# makes a random 6x6 maze that is always solvable
# 2nd build functions
    # function to randomize if walls are present
    # function to check if maze is solvable
    # make sure the start point and end point are set correctly
    # use the path coordinates to check correct wall coordinate in each direction 
# the turtle has to move the same distance it needs to change if the pen is up or down
import turtle
import random

# maze size stuff
rows = 6
cols = 6
cell_size = 50

# making the maze grid with walls
maze = []
for r in range(rows):
    row = []
    for c in range(cols):
        row.append([True, True, True, True])  # top, right, bottom, left
    maze.append(row)

# visited grid 
visited = []
for r in range(rows):
    visited.append([False] * cols)

# turtle setup
def setup_turtle():
    turtle.setup(600, 600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-250, 250)
    turtle.pendown()

# make the walls using recursion (this part is hard!!!)
def walls(x, y):
    visited[y][x] = True
    directions = [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]  # up, right, down, left
    random.shuffle(directions)  # mix it up
       
               
# draw one cell with turtle
def draw_cell(x, y):


# draw the whole maze
def draw_maze():
    setup_turtle()
    walls(0, 0) 

    for row in range(rows):
        for col in range(cols):
            draw_cell(col, row)
            # I thought I needed to move forward here but turns out I don't
            # turtle.forward(cell_size)

    # mark start and end
    turtle.penup()
    turtle.goto(-225, 225)
    turtle.dot(15, "green")  # start
    turtle.goto(-250 + (cols - 1) * cell_size + 25, 250 - (rows - 1) * cell_size - 25)
    turtle.dot(15, "red")    # end

    print("Maze done!")  # just checking

# make sure it is solvable
def is_solvable(row_grid, col_grid):
    size = len(row_grid)
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop()
        if x == size - 1 and y == size - 1:
            return True

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x + 1] == "":
            stack.append((x + 1, y))
        if y < size - 1 and row_grid[y + 1][x] == "":
            stack.append((x, y + 1))
        if x > 0 and col_grid[y][x] == "":
            stack.append((x - 1, y))
        if y > 0 and row_grid[y][x] == "":
            stack.append((x, y - 1))

    return False

# run it
draw_maze()
turtle.done()
