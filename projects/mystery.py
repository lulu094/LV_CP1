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

#
