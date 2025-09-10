#LV 2nd Random Numbers Notes
import random

# Example of random numbers
print(random.random()) # Float betwwen 0 and 1

print(random.randint(1,6))

name = input("What is your name: \n").strip().title()

# Random Stat Creator
stat_one = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_two = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_three = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_four = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_five = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_six = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
stat_seven = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

print(f"Your stat options are: {stat_one},{stat_two},{stat_three},{stat_four},{stat_five},{stat_six},{stat_seven}")

strenght = int(input("Which stat are you making your strength")) + 2