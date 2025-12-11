# LV 2nd Mystery Game

# IMPORTS & INITIAL SETUP  
import random
# Import random for rooms, clues, villains  
# RANDOM(min, max) → returns integer  
# RANDOM() < 0.5 → 50% chance  
#List of game state variables

# List of rooms
# ["Library", "Kitchen", "Hallway", "Basement",  
#  "Training Room", "Puzzle Room", "Camera Room",  
#  "West Wing (Compound)", "East Wing (Compound)"]  
# Compound rooms  
# West wing sub-rooms:  
# ["Storage", "Armory", "Hidden Closet", "Locked Door", "Trap Room", "Fake Passage"] 
# East Wing
# ["Vent Room", "Secret Office", "Decoy Room", "Locked Door", "Trap Room", "Hidden Chamber"] 
rooms = [
    "Library", "Kitchen", "Hallway", "Basement",
    "Training Room", "Puzzle Room", "Camera Room",
    "West Wing (Compound)", "East Wing (Compound)"
]
# Start spot for characters
# SET emma_room TO RANDOM CHOICE between the two compound rooms  
# IF emma_room == "West Wing (Compound)":  
#     kidnapper_room = "East Wing (Compound)"  
# ELSE:  
#     kidnapper_room = "West Wing (Compound)" 
# KIDNAPPER SUB-ROOM: RANDOM CHOICE in possible sub-rooms  
# EMMA SUB-ROOM: ALWAYS behind Locked Door  
compound_rooms = ["West Wing (Compound)", "East Wing (Compound)"]
emma_room = random.choice(compound_rooms)
kidnapper_room = (
    "East Wing (Compound)"
    if emma_room == "West Wing (Compound)"
    else "West Wing (Compound)"
)

kidnapper_subrooms = ["Storage", "Boiler Room", "Hallway", "Guard Post"]
kidnapper_subroom = random.choice(kidnapper_subrooms)
emma_subroom = "Locked Door"

# Player dictionary  
# player["strength_health"] = 100  
# player["logic"] = 10  
# player["intelligence"] = 10  
# player["observation"] = 10  
player_stats = {
    "strength_health": 100,
    "logic": 10,
    "intelligence": 10,
    "observation": 10
}
# Inventory and Clues
# inventory = []  
# clues_found = []  as the game goes the player will find clues
# camera_clue = FALSE  
# key_stolen = FALSE  
# diary_misread = FALSE 
inventory = []
clues_found = []
camera_clue = False
key_stolen = False
diary_misread = False

# Time
# time_minutes = 8 * 60  # Start at 8:00 AM  ends 10 PM
# kidnapper_moving = FALSE  
# kidnapper_murder_attempt = FALSE   
time_minutes = 8 * 60
kidnapper_moving = False
kidnapper_murder_attempt = False

# Utility
# FUNCTION show_time():  
#     hours = time_minutes // 60  
#     mins = time_minutes % 60  
#     PRINT "Current Time: hours:mins AM/PM"  
def show_time(time_minutes):
    hours = time_minutes // 60
    mins = time_minutes % 60

    period = "AM"
    if hours >= 12:
        period = "PM"
    hours = hours % 12
    if hours == 0:
        hours = 12

    print(f"Current Time: {hours}:{mins:02d} {period}")

# FUNCTION advance_time(minutes):  
#     time_minutes += minutes  
#     IF time_minutes >= 21*60 + 45 AND kidnapper_moving == FALSE:  
#         PRINT "The kidnapper has started moving (9:45 PM)!"  
#         kidnapper_moving = TRUE  
#     IF kidnapper_moving == TRUE:  
#         CALL move_kidnapper()  
#     IF time_minutes >= 22*60:  
#         PRINT "It is 10 PM! Emma was not rescued in time!"  
#         GAME OVER  
def move_kidnapper():
    print("The kidnapper moves to a new location...")

def advance_time(time_minutes, kidnapper_moving, minutes_to_advance):
    time_minutes += minutes_to_advance
    show_time(time_minutes)

    if time_minutes >= (21*60 + 45) and not kidnapper_moving:
        print("The kidnapper has started moving (9:45 PM)!")
        kidnapper_moving = True

    if kidnapper_moving:
        move_kidnapper()

    game_over = False
    if time_minutes >= 22 * 60:
        print("It is 10 PM! Emma was not rescued in time!")
        print("GAME OVER")
        game_over = True

    return time_minutes, kidnapper_moving, game_over
# CLUE SYSTEM  
# FUNCTION add_clue(clue):  
#     IF clue NOT IN clues_found:  
#         ADD clue TO clues_found  
#         PRINT "New clue added: (clue)" 
def add_clue(clue, clues_found):
    if clue not in clues_found:
        clues_found.append(clue)
        print(f"New clue added: {clue}")
    return clues_found

# FUNCTION reveal_hidden_clue(clue):  
#     IF "Magnifying Glass" IN inventory OR player["observation"] >= 12:  
#         add_clue(clue)  
#     ELSE:  
#         PRINT "You sense something important… but you miss it."  
def reveal_hidden_clue(clue,inventory,player_stats,clues_found):
    if "Magnifying Glass" in inventory or player_stats["observation"] >=12:
        clues_found = add_clue(clue, clues_found)
    else:
        print("You sense something important... but you miss it.")
    return clues_found

# ITEM & DIARY SYSTEM  
# FUNCTION pick_up(item):  
#     IF item NOT IN inventory:  
#         ADD item TO inventory  
#         PRINT "You picked up: item" 
def pick_up(item, inventory):
    if item not in inventory:
        inventory.append(item)
        print(f"You picked up: {item}")
    else:
        print("You already have this item")
    return inventory

# FUNCTION villain_steal_item():  
#     IF "Master Key" IN inventory AND RANDOM() < 0.25:  
#         REMOVE "Master Key" FROM inventory  
#         key_stolen = TRUE  
#         PRINT "A thief stole your Master Key!"  

def villain_steal_item(inventory,key_stolen):
    if "Master Key" in inventory and random.random()< 0.25:
        inventory.remove("Master Key")
        key_stolen = True
        print("A thief stole your Master Key!")
    return inventory,key_stolen

# FUNCTION read_diary():  
#     IF "Diary" NOT IN inventory:  
#         PRINT "You don't have the diary."  
#         RETURN  
# If player(logic) < if or player ("observation") or if:
#    print "You misread the diary… it gives false directions!"
#    diary_misread = True
#    add_clues = diary_clues - placed in wrong place
# else
#  PRINT "The diary reveals true hints about the wings."  
#  add_clue("Diary: True wing avoids traps and decoys.")  
def read_diary(inventory, player_stats, diary_misread, clues_found):
    if "Diary" not in inventory:
        print("You don't have the diary")
        return diary_misread, clues_found 
    if player_stats("logic") < 12 or player_stats["observation"] < 12:# logic isnt't defined
        print("You misread the diary… it gives false directions!")
        diary_misread = True
    else:
        print("The diary reveals true hints about the wings.")
        clues_found=add_clue("Diary: True wing avoids traps and decoys()")  # assumes add_clue updates clues_found locally
    return diary_misread, clues_found

#FUNCTION use_master_key(subroom):  
#     IF "Master Key" NOT IN inventory:  
#         PRINT "You need the Master Key."  
#         RETURN FALSE  
#     IF key_stolen == TRUE:  
#         PRINT "The Master Key was stolen earlier!"  
#         RETURN FALSE  
#     IF diary_misread == TRUE:  
#         PRINT "You use the Master Key… but misleading clues open a decoy!"  
#         advance_time(15)  
#         RETURN FALSE  
#     PRINT "The Master Key unlocks the door successfully!"  
#     RETURN TRUE  
def use_master_key(inventory, key_stolen, diary_misread, time_minutes, kidnapper_moving):
    if "Master Key" not in inventory:
        print("You need the Master Key.")
        return False, time_minutes, kidnapper_moving
    if key_stolen:
        print("The Master Key was stolen earlier!")
        return False, time_minutes, kidnapper_moving
    if diary_misread:
        print("You use the Master Key… but misleading clues open a decoy!")
        time_minutes, kidnapper_moving, _ = advance_time(time_minutes, kidnapper_moving, 15)
        return False, time_minutes, kidnapper_moving

    print("The Master Key unlocks the door successfully!")
    return True, time_minutes, kidnapper_moving

# FUNCTION combat(villain_power):  
#     PRINT "A villain attacks!"  
#     enemy_health = 20 + villain_power * 2  

#     WHILE TRUE:  
#         dmg = (player["strength_health"] // 10) + RANDOM(1, 6)  
#         enemy_health -= dmg  
#         PRINT "You strike the villain for dmg damage."  

#         IF enemy_health <= 0:  
#             PRINT "Villain defeated!"  
#             IF RANDOM() < 0.3:  
#                 villain_steal_item()  
#             RETURN TRUE  

#         enemy_dmg = villain_power + RANDOM(1, 5) - (player["intelligence"] // 5)  
#         player["strength_health"] -= enemy_dmg  
#         PRINT "Villain hits you for enemy_dmg damage."  

#         IF player["strength_health"] <= 0:  
#             PRINT "You collapsed… Game Over."  
#             GAME OVER  
def combat(villain_power, player_stats, inventory, key_stolen):
    print("A villain attacks!")
    enemy_health = 20 + villain_power *2

    while True:
        dmg = (player_stats["strength_health"] // 10) + random.randint(1, 6)
        enemy_health -= dmg
        print(f"You strike the villain for {dmg} damage.")

        if enemy_health <= 0:
            print("Villain defeated!")
            if "Master Key" in inventory and random.random() < 0.3:
                inventory, key_stolen = villain_steal_item(inventory, key_stolen)
            return True, player_stats, inventory, key_stolen

        enemy_dmg = villain_power + random.randint(1, 5) - (player_stats["intelligence"] // 5)
        player_stats["strength_health"] -= enemy_dmg
        print(f"Villain hits you for {enemy_dmg} damage.")

        if player_stats["strength_health"] <= 0:
            print("You collapsed… Game Over.")
            return False, player_stats, inventory, key_stolen

# KIDNAPPER MOVEMENT SYSTEM  
# FUNCTION move_kidnapper():  
#     IF time_minutes >= 21*60 + 45 AND time_minutes < 22*60:  
#         PRINT "You hear distant footsteps… the kidnapper is moving."  
#         kidnapper_room = RANDOM CHOICE from ROOMS  
#         IF RANDOM() < 0.2:  
#             kidnapper_murder_attempt = TRUE  
#             PRINT "The kidnapper is trying to reach Emma!"  
def move_kidnapper(time_minutes, kidnapper_room, kidnapper_murder_attempt, rooms):
    if 21*60 + 45 <= time_minutes < 22*60:
        print("You hear distant footsteps… the kidnapper is moving.")
        kidnapper_room = random.choice(rooms)
        if random.random() < 0.2:
            kidnapper_murder_attempt = True
            print("The kidnapper is trying to reach Emma!")

    return kidnapper_room, kidnapper_murder_attempt

# FUNCTION check_if_catch_kidnapper(room):  
#     IF room == kidnapper_room AND camera_clue == TRUE:  
#         PRINT "You catch the kidnapper in the act!"  
#         CALL kidnapper_encounter(caught=TRUE)  
def check_if_catch_kidnapper(player_room, kidnapper_room, camera_clue, time_minutes, player_stats, inventory, clues_found):
    if player_room == kidnapper_room and camera_clue:
        print("You catch the kidnapper in the act!")
        kidnapper_encounter(caught=True, time_minutes=time_minutes, player_stats=player_stats,
                            inventory=inventory, clues_found=clues_found)
# 1. OBSERVATION STAT INCREASE SYSTEM
#FUNCTION observatory():
#    PRINT "You enter the Observatory."
#    advance_time(30)
#    player["observation"] += 2
#    PRINT "Your Observation increases by 2!"
#    reveal_hidden_clue("Star charts match markings in one compound wing.")
def observatory(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Observatory. Telescopes and star charts surround you.")
    
    time_minutes, _, _ = advance_time(time_minutes, False, 30)  

    player_stats["observation"] += 2
    print("Your Observation increases by 2!")

    clues_found = reveal_hidden_clue(
        "Star charts match markings in one compound wing.",
        inventory, player_stats, clues_found
    )

    return time_minutes, player_stats, clues_found

# Optional small Observation improvement:
# Add inside camera_room():
# player["observation"] += 1
# PRINT "Observation slightly increased from analyzing the footage."
def camera_room(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Camera Room.")
    time_minutes, _, _ = advance_time(time_minutes, False, 30)

  
    camera_clue = True
    clues_found = add_clue("Camera shows kidnapper was near one wing earlier.", clues_found)

    player_stats["observation"] += 1
    print("Observation slightly increased from analyzing the footage.")

    return time_minutes, player_stats, clues_found, camera_clue
# 2. VILLAINS GUARDING IMPORTANT ITEMS
#FUNCTION villain_guard_item(item):
#    PRINT "A villain blocks your path! He is guarding: ", item
#    result = combat(7)
#    IF result == TRUE:
#        PRINT "You defeat the villain and take:", item
#       pick_up(item)
#    ELSE:
#        PRINT "You fail to obtain the guarded item."
def villain_guard_item(item, player_stats, inventory, clues_found):
    print(f"A villain blocks your path! He is guarding: {item}")
    
    result, player_stats = combat(7, player_stats)
    
    if result:
        print(f"You defeat the villain and take: {item}")
        inventory = pick_up(item, inventory)
    else:
        print("You fail to obtain the guarded item.")
    
    return player_stats, inventory, clues_found
# Example usage inside any room:
# IF RANDOM() < 0.25:
#     villain_guard_item("Master Key")

# 3. EMMA ALWAYS BEHIND THE LOCKED DOOR (EXPLICIT SETUP)
# During setup after choosing emma_room:
#SET emma_subroom TO "Locked Door"
emma_subroom = "Locked Door"
emma_room = random.choice(compound_rooms)
kidnapper_room = (
    "East Wing (Compound)"
    if emma_room == "West Wing (Compound)"
    else "West Wing (Compound)"
)
emma_subroom = "Locked Door"

# 4. TIME-BASED CLUE SYSTEM
#FUNCTION time_based_clue_system(room_name):
#   IF time_minutes < 10*60:
#       add_clue(room_name + " Morning clue: fresh footprints point toward one wing.")
#    ELSE IF time_minutes < 15*60:
#        add_clue(room_name + " Afternoon clue: dust recently disturbed.")
#    ELSE:
#        add_clue(room_name + " Evening clue: faint lantern smell leads toward correct wing.")
def time_based_clue_system(room_name, time_minutes, clues_found):
    if time_minutes < 10 * 60:
        clues_found = add_clue(f"{room_name} Morning clue: fresh footprints point toward one wing.", clues_found)
    elif time_minutes < 15 * 60:
        clues_found = add_clue(f"{room_name} Afternoon clue: dust recently disturbed.", clues_found)
    else:
        clues_found = add_clue(f"{room_name} Evening clue: faint lantern smell leads toward correct wing.", clues_found)
    
    return clues_found

# Example call at the end of any room function:
# time_based_clue_system("Library")


# Insert into kidnapper_encounter() before the luck-based maze section:
#PRINT "Your intelligence cuts through every illusion."
#    PRINT "The kidnapper reveals Emma’s location."
#    YOU WIN

#IF player["logic"] >= 14:
#    PRINT "Your logic exposes the kidnapper’s tricks."
#    PRINT "The illusion maze collapses."
#    YOU WIN

# Only if neither logic nor intelligence is high enough:
# continue to the existing random maze-solve chance.
def kidnapper_encounter(caught, player_stats, camera_clue, time_minutes):
    auto_win = False

    if caught or camera_clue:
        auto_win = True

    if player_stats["intelligence"] >= 14:
        print("Your intelligence cuts through every illusion.")
        print("The kidnapper reveals Emmas location!")
        auto_win = True

    elif player_stats["logic"] >= 14:
        print("Your logic exposes the kidnapper's tricks.")
        print("The illusion maze collapses.")
        auto_win = True

    if auto_win:
        print("Kidnapper defeated psychologically!")
        print("You rescue Emma! YOU WIN")
        return True  

    print("The kidnapper drags you into a maze of riddles…")
   
    if random.random() < 0.3:
        print("You solve the riddle by luck! YOU WIN")
        return True

    print("You fail the maze… the kidnapper escapes. GAME OVER")
    return False  


# ROOM FUNCTIONS (9 ROOMS)  
# FUNCTION library():  
#     PRINT "You enter the Library."  
#     advance_time(30)  
#     IF RANDOM() < 0.4:  
#         pick_up("Diary")  
#         read_diary()  
#     IF time_minutes < 12*60:  
#         reveal_hidden_clue("Early morning dust pattern → wing direction")  
#     ELSE:  
#         PRINT "Books look recently moved…"  
#         add_clue("Someone searched this room today.") 
def library(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Library.")

    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    diary_misread = False 

    if random.random() < 0.4:
        inventory = pick_up("Diary", inventory)
        diary_misread, clues_found = read_diary(
            inventory, player_stats, False, clues_found
        )

    if time_minutes < 12 * 60:
        clues_found = reveal_hidden_clue(
            "Early morning dust pattern, wing direction",
            diary_misread, inventory, player_stats, clues_found
        )
    else:
        print("Books look recently moved…")
        clues_found = add_clue(
            "Someone searched this room today.",
            clues_found
        )

    return time_minutes, player_stats, inventory, clues_found

# Kitchen same thing with all the rooms only slight changes like 
#
#  PRINT "You enter the Kitchen."  
#     advance_time(30)  
#     IF RANDOM() < 0.4:  
#         combat(5)  
#     Else:
#         reveal_hidden_clue("Food crumbs show kidnapper path.")  
def kitchen(time_minutes, player_stats, inventory, clues_found, player_health):
    print("You enter the Kitchen.")

    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    if random.random() < 0.4:
        player_health, villain_defeated = combat(5, player_stats, player_health, inventory)
        if villain_defeated:
            print("You defeated the villain in the Kitchen!")
        else:
            print("The villain overpowered you… Game Over")
            return time_minutes, player_stats, inventory, clues_found, player_health, True  # Game over
    else:
      
        clues_found = reveal_hidden_clue("Food crumbs show kidnapper path.", inventory, player_stats, clues_found)

    return time_minutes, player_stats, inventory, clues_found, player_health, False

# FUNCTION hallway():  
#     PRINT "You enter the Hallway."  
#     advance_time(30)  
#     add_clue("Footsteps lead toward a compound wing.")  
#     IF player["observation"] >= 12:  
#         reveal_hidden_clue("Some footsteps are heavier → villain?")  
def hallway(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Hallway.")

    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    clues_found = add_clue("Footsteps lead toward a compound wing.", clues_found)

    if player_stats["observation"] >= 12:
        clues_found = reveal_hidden_clue("Some footsteps are heavier → villain?", inventory, player_stats, clues_found)

    return time_minutes, clues_found
# FUNCTION basement():  
#     PRINT "You enter the Basement."  
#     advance_time(30)  
#     IF RANDOM() < 0.5:  
#         combat(8)  
#     ELSE:  
#         pick_up("Magnifying Glass")  
def basement(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Basement.")

    # Advance time locally
    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    # Random encounter: villain or item
    if random.random() < 0.5:
        # Combat with villain of power 8
        player_stats, inventory = combat(player_stats, inventory, 8)
    else:
        # Pick up item
        inventory = pick_up("Magnifying Glass", inventory)

    return time_minutes, player_stats, inventory, clues_found
# FUNCTION training_room():  
#     PRINT "You enter the Training Room."  
#     advance_time(30)  
#     player["strength_health"] += 10  
#     PRINT "StrengthHealth increased by 10!"  
def training_room(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Training Room.")

    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    player_stats["strength_health"] += 10
    print("Strength/Health increased by 10!")

    return time_minutes, player_stats, inventory, clues_found

# FUNCTION puzzle_room():  
#     PRINT "You enter the Puzzle Room."  
#     advance_time(30)  
#     IF player["logic"] < 12:  
#         PRINT "The puzzle confuses you… you waste extra time."  
#         advance_time(20)  
#     ELSE:  
#         add_clue("Puzzle reveals false wings have more traps.")  
#     player["logic"] += 2  
#     PRINT "Logic increased!"  
def puzzle_room(time_minutes, player_stats, inventory, clues_found):
    print("You enter the Puzzle Room.")

    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    if player_stats["logic"] < 12:
        print("The puzzle confuses you… you waste extra time.")
        time_minutes, _, _ = advance_time(time_minutes, False, 20)
    else:
        clues_found = add_clue("Puzzle reveals false wings have more traps.", clues_found)

    player_stats["logic"] += 2
    print("Logic increased!")

    return time_minutes, player_stats, inventory, clues_found

# FUNCTION camera_room():  
#     PRINT "You enter the Camera Room."  
#     advance_time(30)  
#     camera_clue = TRUE  
#     add_clue("Camera shows kidnapper was near one wing earlier.")  
def camera_room(time_minutes, player_stats, inventory, clues_found, camera_clue):
    print("You enter the Camera Room.")

    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    camera_clue = True
    clues_found = add_clue("Camera shows kidnapper was near one wing earlier.", clues_found)

    player_stats["observation"] += 1
    print("Observation slightly increased from analyzing the footage.")

    return time_minutes, player_stats, inventory, clues_found, camera_clue

# COMPOUND WINGS (MAIN + SUB-ROOM SYSTEM)  

# FUNCTION west_wing():  
#     PRINT "Entering West Wing."  
#     advance_time(30)  
#     check_if_catch_kidnapper("West Wing (Compound)")  
#     IF RANDOM() < 0.4:  
#         combat(10)  
#     PRINT "Choose a sub-room:"  
#     PRINT west wing sub-rooms  
#     GET choice → subroom  
#     CALL handle_subroom("West Wing", subroom)  
def handle_subroom(wing, room, time_minutes, player_stats, inventory, clues_found):
    print(f"You enter the {room} in the {wing}.")
    if room == "Storage":
        print("You find some old boxes.")
  
    elif room == "Armory":
        print("You see weapons lining the walls.")
       
    elif room == "Hidden Closet":
        print("A small hidden closet, dusty and dark.")
    elif room == "Locked Door":
        print("The door is locked. Maybe you need a key.")
    elif room == "Trap Room":
        print("Careful! This room is trapped.")
  
    elif room == "Fake Passage":
        print("It looks like a passage, but leads nowhere.")
    else:
        print("This room is empty.")

    return time_minutes, player_stats, inventory, clues_found

# FUNCTION east_wing():  
#     PRINT "Entering East Wing."  
#     advance_time(30)  
#     check_if_catch_kidnapper("East Wing (Compound)")  
#     IF RANDOM() < 0.4:  
#         combat(10)  
#     PRINT "Choose a sub-room:"  
#     PRINT east wing sub-rooms  
#     GET choice → subroom  
#     CALL handle_subroom("East Wing", subroom)  
def east_wing(time_minutes, player_stats, inventory, clues_found, camera_clue, player_strength_health):
    print("Entering East Wing.")
    
    time_minutes, _, _ = advance_time(time_minutes, False, 30)

    check_if_catch_kidnapper("East Wing (Compound)", camera_clue)

    if random.random() < 0.4:
        player_strength_health, inventory, key_stolen = combat(player_strength_health, player_stats, inventory)
    east_subrooms = ["Vent Room", "Secret Office", "Decoy Room", "Locked Door", "Trap Room", "Hidden Chamber"]
    print("Choose a sub-room:")
    for i, room in enumerate(east_subrooms):
        print(f"{i + 1}. {room}")

    choice = int(input("Enter sub-room number: ")) - 1
    subroom = east_subrooms[choice]

    time_minutes, player_stats, inventory, clues_found, player_strength_health = handle_subroom(
        "East Wing", subroom, time_minutes, player_stats, inventory, clues_found, player_strength_health
    )

    return time_minutes, player_stats, inventory, clues_found, camera_clue, player_strength_health

# SUB-ROOM HANDLER  
# FUNCTION handle_subroom(wing, subroom):  
#     IF subroom == "Locked Door":  
#         IF use_master_key(subroom) == TRUE:  
#             IF emma_room == wing:  
#                 PRINT "You found Emma! You rescue her!"  
#                 YOU WIN  
#             ELSE IF kidnapper_room == wing:  
#                 CALL kidnapper_encounter(caught=FALSE)  
#             ELSE:  
#                 PRINT "Empty room…"  
#         RETURN  
#     IF subroom == "Trap Room":  
#         PRINT "A trap triggers!"  
#         trap_dmg = RANDOM(5,15) - (player["observation"] // 5)  
#         player["strength_health"] -= trap_dmg  
#         PRINT "You take trap_dmg damage."  
#         IF player["strength_health"] <= 0: GAME OVER  
#         RETURN  
#     IF subroom == "Decoy Room" OR subroom == "Fake Passage":  
#         PRINT "This room is a trick!"  
#         add_clue("This wing contains decoys.")  
#         advance_time(10)  
#         RETURN  
#     IF RANDOM() < 0.3:  
#         combat(7)  
#     reveal_hidden_clue("Strange marks hint at correct wing.")  
def handle_subroom(
    wing, subroom,
    time_minutes, player_stats,
    inventory, clues_found,
    emma_room, kidnapper_room,
    key_stolen, diary_misread,
    camera_clue
):
  
    if subroom == "Locked Door":
        success, time_minutes, _ = use_master_key(
            subroom, inventory, key_stolen, diary_misread, time_minutes, False
        )
        if success:
            if emma_room == wing:
                print("You found Emma! You rescue her!")
                return time_minutes, player_stats, inventory, clues_found, True  # Win
            elif kidnapper_room == wing:
                print("You encounter the kidnapper!")
                kidnapper_encounter(False, player_stats, inventory, clues_found, camera_clue)
            else:
                print("Empty room…")
        return time_minutes, player_stats, inventory, clues_found, False

    elif subroom == "Trap Room":
        print("A trap triggers!")
        trap_dmg = random.randint(5, 15) - (player_stats["observation"] // 5)
        trap_dmg = max(trap_dmg, 0)  
        player_stats["strength_health"] -= trap_dmg
        print(f"You take {trap_dmg} damage.")
        if player_stats["strength_health"] <= 0:
            print("You collapsed… Game Over")
            return time_minutes, player_stats, inventory, clues_found, "GAME OVER"
        return time_minutes, player_stats, inventory, clues_found, False

    elif subroom in ["Decoy Room", "Fake Passage"]:
        print("This room is a trick!")
        clues_found = add_clue(f"{wing} contains decoys.", clues_found)
        time_minutes, _, _ = advance_time(time_minutes, False, 10)
        return time_minutes, player_stats, inventory, clues_found, False


    elif random.random() < 0.3:
        combat_result = combat(7, player_stats, inventory, clues_found)
        if combat_result == "GAME OVER":
            return time_minutes, player_stats, inventory, clues_found, "GAME OVER"

    clues_found = reveal_hidden_clue(
        "Strange marks hint at correct wing.", inventory, player_stats, clues_found
    )

    return time_minutes, player_stats, inventory, clues_found, False

# FINAL KIDNAPPER ENCOUNTER  
# FUNCTION kidnapper_encounter(caught):  
#     PRINT "You confront the kidnapper!"  
#     auto_win = FALSE  

#     IF caught == TRUE:  
#         PRINT "You caught him during his murder attempt!"  
#         auto_win = TRUE  

#     IF camera_clue == TRUE:  
#         PRINT "Camera evidence disrupts his tricks."  
#         auto_win = TRUE  

#     IF player["logic"] >= 14 OR player["intelligence"] >= 14:  
#         PRINT "Your mind resists his illusion maze."  
#         auto_win = TRUE  

#     IF auto_win == TRUE:  
#         PRINT "Kidnapper defeated psychologically!"  
#         PRINT "He reveals Emma’s location!"  
#         YOU WIN  

#     PRINT "The kidnapper drags you into a maze of riddles…"  
#     advance_time(20)  
#     IF time_minutes >= 22*60:  
#         PRINT "You ran out of time!"  
#         GAME OVER  

#     IF RANDOM() < 0.3:  
#         PRINT "You solve the riddle by luck!"  
#         YOU WIN  

#     PRINT "You fail the maze… the kidnapper escapes."  
#     GAME OVER  
def kidnapper_encounter(caught, player_stats, camera_clue, time_minutes):
    print("You confront the kidnapper!")
    auto_win = False

    if caught:
        print("You caught him during his murder attempt!")
        auto_win = True

    if camera_clue:
        print("Camera evidence disrupts his tricks.")
        auto_win = True

    if player_stats.get("logic", 0) >= 14 or player_stats.get("intelligence", 0) >= 14:
        print("Your mind resists his illusion maze.")
        auto_win = True

    if auto_win:
        print("Kidnapper defeated psychologically!")
        print("He reveals Emma's location!")
        return "WIN", time_minutes  

    print("The kidnapper drags you into a maze of riddles…")
    time_minutes, _, _ = advance_time(time_minutes, False, 20)

    if time_minutes >= 22 * 60:
        print("You ran out of time!")
        return "GAME OVER", time_minutes

    if random.random() < 0.3:
        print("You solve the riddle by luck!")
        return "WIN", time_minutes

    print("You fail the maze… the kidnapper escapes.")
    return "GAME OVER", time_minutes


# MAIN GAME LOOP  
# PRINT "WELCOME TO MYSTERY MANSION!"
# PRINT "Find Emma before 10 PM!"  
# WHILE TRUE:  
#     show_time()  
#     PRINT ROOMS  
#     GET user choice  
#     VALIDATE input  
#     selected_room = ROOMS[choice - 1]  

#     IF selected_room == "Library": library()  
#     IF selected_room == "Kitchen": kitchen()  
#     IF selected_room == "Hallway": hallway()  
#     IF selected_room == "Basement": basement()  
#     IF selected_room == "Training Room": training_room()  
#     IF selected_room == "Puzzle Room": puzzle_room()  
#     IF selected_room == "Camera Room": camera_room()  
#     IF selected_room == "West Wing (Compound)": west_wing()  
#     IF selected_room == "East Wing (Compound)": east_wing()  
# END LOOP  
rooms = [
    "Library", "Kitchen", "Hallway", "Basement", "Training Room", 
    "Puzzle Room", "Camera Room", "West Wing (Compound)", "East Wing (Compound)"
]

time_minutes = 8 * 60 
player_stats = {...}   
inventory = [...]      
clues_found = [...]   
player_strength_health = ...  
camera_clue = False    

print("Welcome to Mystery Mansion. You are a detective and have to find Emma before 10:00 p.m.")
print("Save Emma because he is a gentle man, and he is screaming for help!!!")

while True:
    # Show current time formatted (e.g. 8:30 AM)
    hours = time_minutes // 60
    minutes = time_minutes % 60
    print(f"\nCurrent time: {hours:02d}:{minutes:02d}")

    print("Rooms:")
    for i, room in enumerate(rooms, 1):
        print(f"{i}. {room}")

    try:
        choice = int(input("Choose a room by number: "))
        if choice < 1 or choice > len(rooms):
            print("Invalid choice. Please pick a valid room number.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

    selected_room = rooms[choice - 1]

    if selected_room == "Library":
        time_minutes, player_stats, inventory, clues_found = library(time_minutes, player_stats, inventory, clues_found)
    elif selected_room == "Kitchen":
        time_minutes, player_stats, inventory, clues_found = kitchen(time_minutes, player_stats, inventory, clues_found)
    elif selected_room == "Hallway":
        time_minutes, player_stats, inventory, clues_found = hallway(time_minutes, player_stats, inventory, clues_found)
    elif selected_room == "Basement":
        time_minutes, player_stats, inventory, clues_found = basement(time_minutes, player_stats, inventory, clues_found)
    elif selected_room == "Training Room":
        time_minutes, player_stats, inventory, clues_found = training_room(time_minutes, player_stats, inventory, clues_found)
    elif selected_room == "Puzzle Room":
        time_minutes, player_stats, inventory, clues_found = puzzle_room(time_minutes, player_stats, inventory, clues_found)
    elif selected_room == "Camera Room":
        time_minutes, player_stats, inventory, clues_found, camera_clue = camera_room(time_minutes, player_stats, inventory, clues_found, camera_clue)
    elif selected_room == "West Wing (Compound)":
        time_minutes, player_stats, inventory, clues_found, camera_clue, player_strength_health = wing(
            time_minutes, player_stats, inventory, clues_found, camera_clue, player_strength_health)
    elif selected_room == "East Wing (Compound)":
        time_minutes, player_stats, inventory, clues_found, camera_clue, player_strength_health = east_wing(
            time_minutes, player_stats, inventory, clues_found, camera_clue, player_strength_health)

    if time_minutes > 22 * 60:  
        print("You ran out of time! Game over.")
        break