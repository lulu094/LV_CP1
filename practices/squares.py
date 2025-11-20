# LV - CS1400 - Squared Numbers Assignment
# Pseudocode:
# Start with a list of numbers
# Use map() to go through each number
# Square each number using a lambda function
# Print the original number next to its squared value

# List of numbers
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

# Regular function that squares a number (teacher requires one)
def square(num):
    return num ** 2

# Using map() to square every number in the list
# map goes through each number and applies the square function
squared_numbers = list(map(square, numbers))

# Loop through both lists so we can show the original  squared versions
for i in range(len(numbers)):
    print(f"Original: {numbers[i]}, Squared: {squared_numbers[i]}")
