# LV 2nd Order Up
#make a library for drinks,appetizers,soup,special meals, seafood, and desserts
    # cost
    # name of the drinks and rates
    # print the cost and drink ordered


print("Welcome to Puro Peru!")

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
    "Cazuela":6.99,
    "Chupe":10.99
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
    "Tallarines saltados con mariscos" : 19.99,
    "Tallarines verdes con mariscos": 19.99
}

dessert = {
    "Alfajor Clasico": 5.99,
    "Pionono Peruano": 8.99,
    "Arroz con leche": 5.99,
    "Masamorra morada": 5.99
}

# Start order
total = 0
order_drink = ""
order_main = ""
order_sides = []

# Choose drink
#print("\nDrinks:")
#for d in drinks:
    #print(d)
#while True:
    #order_drink = input("Choose a drink: ")
    #if order_drink in drinks:
       # total += drinks[order_drink]
       # break
    #else:
       # print("Sorry, that is not on the menu. Try again.")

# Choose main course
#print("\nMain Courses:")
#main_courses = {}
#main_courses.update(special_meals)
#main_courses.update(seafood)
#for m in main_courses:
    #print(m)
#while True:
    #order_main = input("Choose a main course: ")
    #if order_main in main_courses:
    #    total += main_courses[order_main]
    #    break
    #else:
    #    print("Sorry, that is not on the menu. Try again.")