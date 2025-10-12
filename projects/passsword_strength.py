# LV 2nd Password Strength Checker

# Check for special characters (!@#$%^&*()_+-=[]{}|;:,.<>?)
special_characters = ("!@#$%^&*()_+-=[]{}|;:,.<>?")
# Set score
length = False
uppercase = False
lowercase = False
numbers = False
special_characters = False
# Check for requirements 
    #Length: At least 8 characters long
    #use len(list_name)
        #if true
        #score +1
    #Uppercase: Contains at least one uppercase letter
        #if true
            #score +1
    #Lowercase: Contains at least one lowercase letter
        #if true
            #score +1
    #Numbers: Contains at least one number
        #if true
            #score +1
    #Special characters: Contains at least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)
        #if true
            #score +1
# 
# if requirements True
        # print - sum of the total score, password strenght, contains lowercase
