# LV 2nd Functions

num = 0
player_hp = 100
monster_hp = 100

def add(x, y):
    return x + y

def initials(name):
    names = name.split(" ")  # FIXED: split("") → split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    global player_hp, monster_hp  # Needed to modify outer variables
    if turn == "player":
        monster_hp -= dmg
    else:
        player_hp -= dmg
    return monster_hp, player_hp

while num < add(5, 5):    
    print("Duck")
    num += 1

print("Goose")  # FIXED: Spelling
print(f"Result is: {add(1, 1)}")  # FIXED: "Results is" → "Result is"
total = add(1, 1)

print(add(add(3.14, 0.85), 10))

add(42, 7)

print(f"Tia's initials are: {initials('Tias LaRose')}")
print(f"Bob's initials are: {initials('Bob LaRose')}")

monster_hp, player_hp = attack(15, "player")

print(f"Player health: {player_hp}")
print(f"Monster health: {monster_hp}")
