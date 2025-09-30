# LV 2nd Shopping List Manager
shopping_list = []

#Put your shopping list variable here
while True:
    action = input("What do you want to do (add,remove,view,exit)").lower()#user input with instructions
    #Write your code here
    if action == "add":
        item = input("What item do you want to add? ")
        shopping_list.append(item)
        #add item to your shopping list
        print(f"{item} has been added to the list")
    elif action == "remove":
        item = input("What item do you want to remove? ")
        shopping_list.remove(item)
        #remove item from your shopping list
        print(f"{item} has been removed from the list")
    elif action == "view":
        print("Your shopping list contains:")
        for item in shopping_list:
            print(f"- {item}")
        #view all items in your shopping list
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please choose add, remove, view, or exit.")