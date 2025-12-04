# LV 2nd Mystery Game

# IMPORTS & INITIAL SETUP  
# Import random for randomness in rooms, clues, villains  
# RANDOM(min, max) → returns integer  
# RANDOM() < 0.5 → 50% chance  

# Introduce the player to the game
# print "Welcome to ... This are the rules .... and goals..."

# List of rooms
# ["Library", "Kitchen", "Hallway", "Basement",  
#  "Training Room", "Puzzle Room", "Camera Room",  
#  "West Wing (Compound)", "East Wing (Compound)"]  
# Compound rooms  
# West wing sub-rooms:  
# ["Storage", "Armory", "Hidden Closet", "Locked Door", "Trap Room", "Fake Passage"] 
# East Wing
# ["Vent Room", "Secret Office", "Decoy Room", "Locked Door", "Trap Room", "Hidden Chamber"]  

# Start spot for characters
# SET emma_room TO RANDOM CHOICE between the two compound rooms  
# IF emma_room == "West Wing (Compound)":  
#     kidnapper_room = "East Wing (Compound)"  
# ELSE:  
#     kidnapper_room = "West Wing (Compound)" 
# KIDNAPPER SUB-ROOM: RANDOM CHOICE in possible sub-rooms  
# EMMA SUB-ROOM: ALWAYS behind Locked Door  

# Player dictionary  
# player["strength_health"] = 100  
# player["logic"] = 10  
# player["intelligence"] = 10  
# player["observation"] = 10  

# Inventory and Clues
# inventory = []  
# clues_found = []  as the game goes the player will take clues
# camera_clue = FALSE  
# key_stolen = FALSE  
# diary_misread = FALSE 

# Time
# time_minutes = 8 * 60  # Start at 8:00 AM  ends 10 PM
# kidnapper_moving = FALSE  
# kidnapper_murder_attempt = FALSE   

# Utility
# FUNCTION show_time():  
#     hours = time_minutes // 60  
#     mins = time_minutes % 60  
#     PRINT "Current Time: hours:mins AM/PM"  

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

# CLUE SYSTEM  
# FUNCTION add_clue(clue):  
#     IF clue NOT IN clues_found:  
#         ADD clue TO clues_found  
#         PRINT "New clue added: (clue)"  

# FUNCTION reveal_hidden_clue(clue):  
#     IF "Magnifying Glass" IN inventory OR player["observation"] >= 12:  
#         add_clue(clue)  
#     ELSE:  
#         PRINT "You sense something important… but you miss it."  

# ITEM & DIARY SYSTEM  
# FUNCTION pick_up(item):  
#     IF item NOT IN inventory:  
#         ADD item TO inventory  
#         PRINT "You picked up: item"  

# FUNCTION villain_steal_item():  
#     IF "Master Key" IN inventory AND RANDOM() < 0.25:  
#         REMOVE "Master Key" FROM inventory  
#         key_stolen = TRUE  
#         PRINT "A thief stole your Master Key!"  

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

# COMBAT SYSTEM  
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

# KIDNAPPER MOVEMENT SYSTEM  
# FUNCTION move_kidnapper():  
#     IF time_minutes >= 21*60 + 45 AND time_minutes < 22*60:  
#         PRINT "You hear distant footsteps… the kidnapper is moving."  
#         kidnapper_room = RANDOM CHOICE from ROOMS  
#         IF RANDOM() < 0.2:  
#             kidnapper_murder_attempt = TRUE  
#             PRINT "The kidnapper is trying to reach Emma!"  

# FUNCTION check_if_catch_kidnapper(room):  
#     IF room == kidnapper_room AND camera_clue == TRUE:  
#         PRINT "You catch the kidnapper in the act!"  
#         CALL kidnapper_encounter(caught=TRUE)  

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

# Kitchen same thing with all the rooms only slight changes like 
#
#  PRINT "You enter the Kitchen."  
#     advance_time(30)  
#     IF RANDOM() < 0.4:  
#         combat(5)  
#     Else:
#         reveal_hidden_clue("Food crumbs show kidnapper path.")  



# FUNCTION hallway():  
#     PRINT "You enter the Hallway."  
#     advance_time(30)  
#     add_clue("Footsteps lead toward a compound wing.")  
#     IF player["observation"] >= 12:  
#         reveal_hidden_clue("Some footsteps are heavier → villain?")  


# FUNCTION basement():  
#     PRINT "You enter the Basement."  
#     advance_time(30)  
#     IF RANDOM() < 0.5:  
#         combat(8)  
#     ELSE:  
#         pick_up("Magnifying Glass")  


# FUNCTION training_room():  
#     PRINT "You enter the Training Room."  
#     advance_time(30)  
#     player["strength_health"] += 10  
#     PRINT "StrengthHealth increased by 10!"  


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


# FUNCTION camera_room():  
#     PRINT "You enter the Camera Room."  
#     advance_time(30)  
#     camera_clue = TRUE  
#     add_clue("Camera shows kidnapper was near one wing earlier.")  


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