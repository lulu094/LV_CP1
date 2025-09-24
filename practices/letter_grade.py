# LV 2nd Grade

# Ask the user for a grade percentage (0-100)
grade = float(input("Enter your grade percentage (0-100): "))

# Print the letter of the grade 94 a, 90 a-, 87 b+, 84 b, 80 b-, 77 c+, 74 c, 70 c-, 67 d+, 64 d, 60 d-, below 60 f
if grade >= 94:
    print("Your letter grade is: A.")
elif grade >= 90:
    print("Your letter grade is: A-.")
elif grade >= 87:
    print("Your letter grade is: B+.")
elif grade >= 84:
    print("Your letter grade is: B.")
elif grade >= 80:
    print("Your letter grade is: B-.")
elif grade >= 77:
    print("Your letter grade is: C+.")
elif grade >= 74:
    print("Your letter grade is: C.")
elif grade >= 70:
    print("Your letter grade is : C-.")
elif grade >= 67:
    print("Your letter grade is: D+.")
elif grade >= 64:
    print("Your letter grade is: D.")
elif grade >= 60:
    print("Your letter grade is: D-.")
else:
    print("Your letter grade is: F.")
