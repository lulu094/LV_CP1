# LV 2nd grade calculator
grade_math = float(input("What is your grade in math?"))
grade_programming = float(input("What is your grade in programming?"))
grade_biology = float(input("What is your grade in biology?"))
grade_advisory = float(input("What is your grade in advisory"))
grade_english = float(input("What is your grade in english?"))
grade_drawing = float(input("What is your grade in drawing?"))
grade_worldciv = float(input("What is your grade in worldciv?"))

average_grade = (grade_math + grade_programming +grade_biology + grade_advisory + grade_english + grade_drawing + grade_worldciv)/7

print("Your average grade is:", round(average_grade,2))