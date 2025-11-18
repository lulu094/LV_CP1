# LV 2nd Flexible Calculator

# Define a function called calculator
# *numbers will take any amount of numbers the user gives us
# **info will take extra information as keyword arguments, like the operation
#def calculator(*numbers, **info):

    # Extract the operation from the keyword arguments
    # info is like a dictionary: info["operation"] gives the value
    # For example, if we call calculator(1,2,3, operation="sum"), this line stores "sum" in operation
    #operation = info["operation"]

    # Check what operation the user wants
    # Then perform the correct calculation

   # if operation == "sum":
        # sum() is a built-in function that adds all numbers together
        #return sum(numbers)

    #if operation == "average":
        # sum(numbers) adds them, len(numbers) counts how many numbers there are
        # Dividing gives the average
       # return sum(numbers) / len(numbers)

    #if operation == "max":
        # max() finds the largest number
        #return max(numbers)

   """ if operation == "min":
        # min() finds the smallest number
        return min(numbers)
"""
    #if operation == "product":
        # Product means multiplying all numbers together
        # Start with 1 (because multiplying by 0 would give 0)
        #product = 1
        # Go through each number one by one
        #for n in numbers:
            #product *= n   # Multiply product by this number
       # return product


# Main loop so the program keeps running until the user quits
#while True:
    # Ask the user which operation they want
    #operation_choice = input("\nChoose an operation (sum, average, max, min, product): ").lower()

    # Create an empty list to store numbers
    #numbers = []

    # Explain to the user how to enter numbers
    #print("Enter numbers one at a time. Type 'done' when finished.")

    # Loop to collect numbers
    #while True:
      #  user_input = input("Number: ")

        #if user_input.lower() == "done":
            # Stop collecting numbers when the user types 'done'
           # break

       # try:
            # Convert the input to a float (decimal number)
            # If the user typed something invalid, this will fail and go to except
           # numbers.append(float(user_input))
        #except:
            # Tell the user their input was invalid
           # print("Invalid number. Please try again.")

    # If no numbers were entered, remind the user and restart
    """if len(numbers) == 0:
        print("You must enter at least one number.")
        continue
"""
    # Call the calculator function
    # *numbers sends all the numbers as separate arguments (1,2,3,...) to *args
    # operation=operation_choice sends the operation as a keyword argument to **kwargs
   # result = calculator(*numbers, operation=operation_choice)

    # Show the result to the user
    #print(f"\nResult: {result}")

    # Ask if the user wants to do another calculation
    """again = input("Would you like to do another calculation? (yes/no): ").lower()
    if again != "yes":
        # End the program if they don't want to continue
        print("Thank you for using the Flexible Calculator!")
        break"""
