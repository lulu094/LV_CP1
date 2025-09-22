# LV 2nd User Sign in

# Predefined username and password
user_name = "student"
user_password = "lulu24"

# Ask for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Checking if the user is signed in correctly
if username == user_name and password == user_password:
    print("Welcome!")
else:
    print("Error, please try again later.")