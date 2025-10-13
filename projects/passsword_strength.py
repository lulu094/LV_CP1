# LV 2nd Password Strength Checker

# Ask the user to input a password
# This is where the program receives input from the user
password = input("Enter a password: ")

# Initialize the score
# The score will increase based on how many requirements the password meets (max score = 5)
score = 0

# Set up flags for each requirement
# These variables will be used to store whether or not the password meets each condition
length = False       # Will be True if password is 8+ characters
uppercase = False    # Will be True if password has at least one uppercase letter
lowercase = False    # Will be True if password has at least one lowercase letter
numbers = False      # Will be True if password has at least one digit
special = False      # Will be True if password has at least one special character

# Define what counts as a special character
# This is the list of symbols we consider as special characters for the password
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

# Check password requirements one by one

# Check if password length is at least 8 characters
# This is a basic security rule — longer passwords are usually harder to guess
if len(password) >= 8:
    length = True      # Mark this rule as passed
    score += 1         # Add 1 point to the password strength score
# Check if password contains at least one uppercase letter
# This helps make passwords more complex and secure
if any( char.isupper() for char in password):
    uppercase = True
    score += 1
# Check if password contains at least one lowercase letter
# Required to ensure the password isn’t all uppercase or numbers
if any( char.islower() for char in password):
    lowercase = True
    score += 1
# Check if password contains at least one number
# Including digits adds variety and strength to the password
if any( char.isdigit() for char in password):
    numbers = True
    score += 1
# Check if password contains at least one special character
# Special characters increase password complexity and reduce the chance of it being cracked
if any( char in special_characters for char in password):
    special = True
    score += 1
# Output results of checks

# Show a checklist of what the password includes
# This helps the user understand which rules they met and which ones they missed
print("\n Password strength:")
print(f"Length ")
print(f"")
print(f"")
print(f"")
print(f"")
print(f"")
# Display final strength score

# Show the user how many points out of 5 their password earned

# Give final feedback based on score
# Use if/elif statements to give a final message depending on the total score
if score <= 2:
    print(f"You have a weak password")
elif score == 3:
    print(f"You have a moderate password")
elif score == 4:
    print(f"You have a strong password")
else:
    print(f"You have a very strong password!")