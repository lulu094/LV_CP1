# JD - CS1400A - Combat Program

import random

# --- Step 1: Get user stats ---
print("Welcome to training! First I need to know some things about you!")

name = input("What is your name? ")

print("\nWhat class of fighter are you?")
print("1 = Fighter")
print("2 = Mage")
print("3 = Rogue")

choice = int(input("Choose your class (1-3): "))

# Assign stats based on class
if choice == 1:
    player = {"class": "Fighter", "health": 30, "defense": 14, "attack": 5, "damage": 8}
elif choice == 2:
    player = {"class": "Mage", "health": 25, "defense": 10, "attack": 7, "damage": 10}
else:
    player = {"class": "Rogue", "health": 28, "defense": 12, "attack": 6, "damage": 6}

print(f"\nGreat, here are your stats {name} the {player['class']}!")
print(f"Health: {player['health']}")
print(f"Defense: {player['defense']}")
print(f"Attack: +{player['attack']}")
print(f"Damage: D{player['damage']}")

# --- Step 2: Create Monster ---
monster = {"name": "Dire Wolf", "health": 30, "defense": 13, "attack": 4, "damage": 6}
print(f"\nYou are being attacked by a {monster['name']}!")

# --- Step 3: Randomize first move ---
if random.choice(["player", "monster"]) == "player":
    print("\nYou move first!")
    turn = "player"
else:
    print("\nThe monster moves first!")
    turn = "monster"

# --- Step 4: Define functions ---
def user_turn():
    """Handles all user combat options"""
    global player, monster
    print("\nWhat would you like to do?")
    print("1. Normal Attack")
    print("2. Wild Attack (double damage but take self-damage)")
    print("3. Drink a healing potion (+9 HP)")
    print("4. Flee")

    choice = int(input("> "))

    if choice == 1:
        dmg = random.randint(1, player["damage"]) + player["attack"]
        print(f"You hit for {dmg} damage!")
        monster["health"] -= dmg
    elif choice == 2:
        dmg = (random.randint(1, player["damage"]) + player["attack"]) * 2
        print(f"You go berserk! You hit for {dmg} damage, but hurt yourself!")
        monster["health"] -= dmg
        player["health"] -= random.randint(2, 6)
    elif choice == 3:
        heal = 9
        player["health"] += heal
        print(f"You drink a potion and heal {heal} HP!")
    elif choice == 4:
        if random.random() < 0.5:
            print("You successfully fled the battle!")
            return "fled"
        else:
            print("You failed to flee!")
    return "continue"

def monster_turn():
    """Handles the monster's attack"""
    global player, monster
    dmg_roll = random.randint(1, monster["damage"]) + monster["attack"]
    print(f"The {monster['name']} attacks you for {dmg_roll} damage!")
    player["health"] -= dmg_roll

# --- Step 5: Combat Loop ---
while player["health"] > 0 and monster["health"] > 0:
    print("\n----------------------------")
    print(f"{name}'s HP: {player['health']} | {monster['name']} HP: {monster['health']}")
    print("----------------------------")

    if turn == "player":
        result = user_turn()
        if result == "fled":
            break
        turn = "monster"
    else:
        monster_turn()
        turn = "player"

# --- Step 6: Display Winner ---
print("\n===== Combat Over =====")
if player["health"] <= 0:
    print(f"{name} was defeated by the {monster['name']}...")
elif monster["health"] <= 0:
    print(f"You defeated the {monster['name']}! Congratulations, {name}!")
else:
    print("You escaped the battle safely!")
