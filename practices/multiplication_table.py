# LV 2nd Multiplication Table

#Print header row (numbers 1 to 12)
print("    ", end= "")#Spacing for the top-left corner
for i in range(1,13):#Loop through numbers 1 to 12
    print(f"{i:4}", end= "") #Print the too header numbers with spacing
print()#Move to a new line

#Print separator line
print("    " + "-" * (4*12))#Print a line of dashes for separation
#Print each row of the multiplication table
for i in range(1,13):#Loop through numbers 1 to 12 for rows
    print(f"{i:2} |", end= "")#Print the row header number with spacing
    for j in range(1,13):#Loop through numbers 1 to 12 for columns
        print(f"{i*j:4}", end= "")#Print the product of the row and column numbers with spacing
    print()#Move to a new line after each row