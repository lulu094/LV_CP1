# LV 2nd Functioms

num = 0
player_hp = 100
monster_hp = 100


def add(x,y):
    return x+y

def initials(name):
    names = name.split("")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn =="player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp- dmg


#while num < add(5,5)    
   # print("Duck")
   # num += 1
#print("Gose")
#print(f"Results is: {add(1,1)} ")
#total = add(1,1)
#print(ad(add(3.14,.85),10))
#add(42,7)

print(f"Tia's iniitials are:{initials("Tias LaRose")}")
print(f"Bob's iniitials are:{initials("Bob LaRose")}")
monster_hp, player_hp = attack(15, monster_hp)
print(f"player helath:{player_hp}")
print(f"monster helath:{monster_hp}")

#acces to the numbers 
#function combined with a for loop
print(f"a= {ord("a")}")
print(f"100 = {chr(100)}")