# LV 2nd Conditionals Notes

import random
monster_hp = 30
dmg_modifier = 2
atk_bonus = 3
player_hp = 25

roll = random.randint (1,20)

if roll == 20:
    print("You rolled a crit! double your damage.")
    attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll+atk_bonus > 10:
    print(f"You hit")
    attack = random.randint(1,8) +dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll == 20:
    print("You got the highest number possible! ")
elif roll <= 10:
    if roll == 1:
        print(f"You  rolled a critical failure! The monster gets a free attack!")
        damage = (random.randint(1,10) + 2)
        player_hp -= damage
        print(f"Ypu tppl {damage} you now jhave {player_hp} HP.")
    else:
        print("You missed!")
else:
    print("That shouldn't be possible")

print("Your turn is over.")

if monster_hp:
    print("It is the mosnters turn")
else:
    print("the monster is dead")
    