# LV 2nd Basic Calculator

# Get input from the user
num1 =(input("Enter the first number:"))
num2 =(input("Enter the second number:"))


#Print results using d-strings and rounding to 2 decimal places
print(f"{num1}+{num2}={round(num1 + num2,2)}")
print(f"{num1}-{num2}={round(num1 - num2,2)}")
print(f"{num1}*{num2}={round(num1 * num2,2)}")
print(f"{num1}/{num2}={round(num1 / num2,2)}")
print(f"{num1}//{num2}={round(num1 // num2,2)}")
print(f"{num1}%{num2}={round(num1 % num2,2)}")
print(f"{num1}**{num2}={round(num1 ** num2,2)}")
