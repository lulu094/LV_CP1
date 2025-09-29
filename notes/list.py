#LV 2nd List Notes

import random 

name = ["Alex", "Katie", "Cora", "Andrew","Jake","Eric", 5,3.14, False]

print(name)
print(name[3])
print(name[random.randint(1,len(name))])
print(random.choice(name))
name[-1] = "Xavier"
name.extend(["Treyson", "Tia"])
name += ["Joseph", "Isreal", "Zee"]
name.remove(3.14)
x = name.index(5)
name.pop(x)
print(name)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

board[1][1] = "X"

print(board)
#List(changable, ordered)
#Tuple(unchangable, ordered)
classes = ("Bard", "Monk","Barbarian","Paladin")

#Set (changable, unorderd)
fruits = {"Apple", "Strawberry", "Orange", "Grapes"}
print(fruits)
