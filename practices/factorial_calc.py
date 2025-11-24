# LV 2nd Factorial Calculator
#Emma's pseudocde
# Welcome the user
# User inputs
#Use int( ) or str() to make sure they use numbers
# Use if statements to make sure it is true
# else say its an invalid input, make user.type a number continue the code
#ask user if it wants to put another number
# (original # * og#-1, og#-2 till you get to one) = answer
# print out the numbers inputed by the User
#when user types "done"
#print ( thank you for using the calculator)

print("Welcome to Factorial Calculator!")   
# Welcome the user
# (already done above)

# User inputs
while True:                                            
    original = input("Enter a number to calculate its factorial (or type 'done' to exit): ")

#Use int( ) or str() to make sure they use numbers
    # actual code checks input below

# Use if statements to make sure it is true
    if original.lower() == "done":                   
        break

# else say its an invalid input, make user.type a number continue the code
    if not original.isdigit():                       
        print("Invalid input. Please type a number.")
        continue

#ask user if it wants to put another number
    num = int(original)                              
    factorial = 1

# (original # * og#-1, og#-2 till you get to one) = answer
    while num > 1:                                    
        factorial *= num
        num -= 1

# print out the numbers inputed by the User
    print(f"The factorial of {original} is: {factorial}")  
#when user types "done"
# (handled above)

#print ( thank you for using the calculator)
print("Thank you for using the calculator!")          