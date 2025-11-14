# LV 2nd Order Up
# The program lets the user order from a Peruvian menu
# Menu items are stored in dictionaries with their prices
# The user chooses a drink, a main course, and two side dishes
# Input is checked using a helper function that matches words even in lowercase
# The program adds up the cost as the user selects valid items
# At the end, the user's full order and total cost are displayed

print("Welcome to Puro Peru!")

# Menu dictionary
drinks = {
    "Inca Kola": 4.81,
    "Coca Cola ": 3.59,
    "Chicha Morada": 3.50,
    "Sprite": 2.99
}

appetizer = {
    "Causa Rellena": 18.99,
    "Tamal Peruano": 8.99,
    "Anticucho Tradicional": 9.99,
    "Papa rellena": 18.99
}

soups = {
    "Sopa Criolla": 10.99,
    "Sopa de Paico": 12.99,
    "Cazuela": 6.99,
    "Chupe": 10.99
}

special_meals = {
    "Desayuno Lurin": 17.00,
    "Chicharron de chancho": 12.99,
    "Chicharron de pollo": 12.99,
    "Chicharron de pescado": 12.99
}

seafood = {
    "Pescado a lo macho": 19.99,
    "Saltado de camarones": 15.99,
    "Tallarines saltados con mariscos": 19.99,
    "Tallarines verdes con mariscos": 19.99
}

dessert = {
    "Alfajor Clasico": 5.99,
    "Pionono Peruano": 8.99,
    "Arroz con leche": 5.99,
    "Masamorra morada": 5.99
}

# Helps find the match quicker
def find_item(user_input, menu_dict):
    user_input = user_input.strip().lower()
    for item in menu_dict:
        if item.lower() == user_input:
            return item
    return None

# Start Order
total = 0

# Drinks
print("\nDrinks:")
for d in drinks:
    print(d)

while True:
    user = input("Choose a drink: ")
    drink = find_item(user, drinks)
    if drink:
        total += drinks[drink]
        break
    else:
        print("Please choose something from the menu.")

# Main course 
print("\nMain Courses:")
main_courses = {}
main_courses.update(special_meals)
main_courses.update(seafood)

for m in main_courses:
    print(m)

while True:
    user = input("Choose a main course: ")
    main = find_item(user, main_courses)
    if main:
        total += main_courses[main]
        break
    else:
        print("Please choose something from the menu.")

# Side Dishes
print("\nSide Dishes:")
side_dishes = {}
side_dishes.update(appetizer)
side_dishes.update(soups)

for s in side_dishes:
    print(s)

while True:
    user = input("Choose side #1: ")
    side1 = find_item(user, side_dishes)
    if side1:
        total += side_dishes[side1]
        break
    else:
        print("Please choose something from the menu.")

while True:
    user = input("Choose side #2: ")
    side2 = find_item(user, side_dishes)
    if side2:
        total += side_dishes[side2]
        break
    else:
        print("Please choose something from the menu.")

# Printing  order
print("\nYour order:")
print("Drink:", drink)
print("Main Course:", main)
print("Side Dishes:")
print("-", side1)
print("-", side2)
print("Total Cost: $", round(total, 2))
