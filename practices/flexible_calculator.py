# LV 2nd Flexible Calculator

# Define a function called calculator
# *numbers will take any amount of numbers the user gives us
# **info will take extra information as keyword arguments, like the operation
def calculator(*numbers, **info):
   
    # hacer las operaciones matematicas de alguna forma u otra
    # 
    # agregar las ecuaciones de alguna forma
    # je nais se pais!!!!!
    # Extract the operation from the keyword arguments
    # info is like a dictionary: info["operation"] gives the value
    # For example, if we call calculator(1,2,3, operation="sum"), this line stores "sum" in operation
    operation = info["operation"]
    
print("Welcome to Flexible Calculator!")
    # Check what operation the user wants
    # Then perform the correct calculation


# Main loop so the program keeps running until the user quits
while True:
    # Ask the user which operation they want
    print("Which operation would you like to perform (sum, average, max, min, product)?")
    
    # Create an empty list to store numbers
   

    # Explain to the user how to enter numbers
   
    # Loop to collect numbers
    #while True:
     

    # Call the calculator function
    # *numbers sends all the numbers as separate arguments (1,2,3,...) to *args
    # operation=operation_choice sends the operation as a keyword argument to **kwargs

    # Show the result to the user
    #print(f"\nResult: {result}")

    # Ask if the user wants to do another calculation
    # if so then repeat the whole loop
    print("Would you like to perform another calculation?")
