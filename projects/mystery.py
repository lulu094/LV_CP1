# LV 2nd Mystery Game
# import random
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

# Master Key
# if master key and clue
#   door opens

# Time
# time_minutes = 8 * 60  # Start at 8:00 AM  ends 10 PM
# kidnapper_moving = FALSE  
# kidnapper_murder_attempt = FALSE   

# Utility
# FUNCTION show_time():  
#     hours = time_minutes // 60  
#     mins = time_minutes % 60  
#     PRINT "Current Time: hours:mins AM/PM"  

# Health
# 