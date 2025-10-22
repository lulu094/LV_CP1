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

# FIXED: Missing colon at end of while loop
while num < add(5, 5):    
    print("Duck")
    num += 1

print("Goose")  # FIXED: Spelling
print(f"Result is: {add(1, 1)}")  # FIXED: "Results is" → "Result is"
total = add(1, 1)

# FIXED: Typo - 'ad' → 'add'
print(add(add(3.14, 0.85), 10))

# This call has no output, which is fine unless you wanted to store or print it:
add(42, 7)

# FIXED: Nested quotes and spelling
print(f"Tia's initials are: {initials('Tias LaRose')}")
print(f"Bob's initials are: {initials('Bob LaRose')}")

# FIXED: Wrong argument passed to attack() — should be 'player' or 'monster'
monster_hp, player_hp = attack(15, "player")

# FIXED: Spelling
print(f"Player health: {player_hp}")
print(f"Monster health: {monster_hp}")
