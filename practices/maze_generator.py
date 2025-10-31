# LV 2nd Maze Generator

#Importing libraries
import random
import turtle

# Make a list  to make an invisible 6x6 grid, yhat the turtle will just go through to draw the maze
print("    " + "-" * (6*6))
for i in range(1,13):#Loop through numbers 1 to 12 for rows
    print(f"{i:2} |", end= "")#Print the row header number with spacing
    for j in range(1,13):#Loop through numbers 1 to 12 for columns
        print(f"{i*j:4}", end= "")#Print the product of the row and column numbers with spacing
    print()#Move to a new line after each row