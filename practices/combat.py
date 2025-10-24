# LV 2nd Combat
import random
Health = 0
Defense = 0
Attack = 0
Damage = 0
fighter = 1
Merge = 2
Rouge = 3
player_hp = 0
monster_hp = 0
print("Welcome to training! First I need to know some things about you!")

name = input("What is your name:")
user_fighter = ("What class of fighter are you ( 1 if you are a Fighter, 2 if you are a Merge, 3 if you are a Rouge):")
print(fighter)

def attack(dmg, turn):
    global player_hp, monster_hp  # Needed to modify outer variables
    if turn == "player":
        monster_hp -= dmg
    else:
        player_hp -= dmg
    return monster_hp, player_hp

if monster_hp:
    health = 0
    defense = 0
    attack = 0
    Damage = 0
if user_fighter - 1:
    health = 0
    defense = 0
    attack = 0
    damage = 0
