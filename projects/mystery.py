# LV 2nd Mystery Game
# Import
# for random choices and random events


# Define rooms
# CREATE a list called "rooms" containing:
    #""Library", "Kitchen", "Hallway", "Basement",
    #"Training Room", "Puzzle Room", "Camera Room",
    #"West Wing (Compound)", "East Wing (Compound)"


# Assign a room for Emma and the Kidnapper


#SET emma_room TO RANDOM CHOICE between "West Wing (Compound)" AND "East Wing (Compound)"
#IF emma_room IS "West Wing (Compound)":
    #SET kidnapper_room TO "East Wing (Compound)"
#ELSE:
    #SET kidnapper_room TO "West Wing (Compound)"


#Create inventory and clues
# CREATE empty list called inventory  # stores items player picks up
# CREATE empty list called clues_found  # stores clues player discovers


# Player Stats


#CREATE dictionary called player with keys:
# current health 100
# affects combat damage 10
# helps understand clues and avoid traps 10
# helps solve riddles and spot fake clues 10


#Set the time
#SET time_minutes TO 8 * 60  # starting at 8:00 AM




# UTILITY FUNCTIONS


#DEFINE FUNCTION show_time():
    # Calculate hours and minutes from total minutes
    #SET hours TO time_minutes DIVIDED BY 60
    #SET mins TO time_minutes MODULO 60


    # Determine AM/PM period
    #IF hours == 0:
        #SET display_hour TO 12
        #SET period TO "a.m."
    #ELSE IF 1 <= hours < 12:
        #SET display_hour TO hours
        #SET period TO "a.m."
    #ELSE IF hours == 12:
        #SET display_hour TO 12
        #SET period TO "p.m."
    #ELSE:
        #SET display_hour TO hours - 12
        #SET period TO "p.m."


    #PRINT "Current Time: display_hour : mins period"


#DEFINE FUNCTION advance_time(minutes):
    # Increase game time by specified minutes
    #ADD minutes TO time_minutes
    # Check if time exceeds 10 PM
    #IF time_minutes >= 22 * 60:
       # PRINT "Time reached 10 PM! Emma was not rescued!"
       # PRINT "GAME OVER"
       # EXIT game


#DEFINE FUNCTION add_clue(clue):
    # Add a new clue if it hasn't been found yet
    #IF clue NOT IN clues_found:
        #ADD clue TO clues_found
        #PRINT " New clue added: clue"


# Combat System


#DEFINE FUNCTION combat(villain_strength):
    #PRINT "A villain attacks!"


    # Calculate villain's health based on strength
    #SET enemy_health TO 20 + villain_strength * 2
    #WHILE TRUE:
        # Player attacks villain
        #SET dmg TO player["strength"] + RANDOM INTEGER between 1 AND 6
        #SUBTRACT dmg FROM enemy_health
        #PRINT "You hit the villain for dmg damage (Enemy HP: enemy_health)"


        # Check if villain is defeated
        #IF enemy_health <= 0:
            #PRINT "Villain defeated!"
            #RETURN TRUE  # exit combat loop


        # Villain attacks player
        #SET enemy_dmg TO villain_strength + RANDOM INTEGER between 1 AND 5
        #SUBTRACT enemy_dmg FROM player["health"]
        #PRINT "The villain hits you for enemy_dmg damage (Your HP: player['health'])"


        # Check if player dies
        #IF player["health"] <= 0:
            #PRINT "You died. GAME OVER"
            #EXIT game


# Items


#DEFINE FUNCTION pick_up(item):
    # Add item to inventory if not already there
    #IF item NOT IN inventory:
        #ADD item TO inventory
        #PRINT "You picked up item"


# Room functions


#DEFINE FUNCTION library():
    #PRINT "You enter the Library"
    #CALL advance_time(30)  # spend 30 minutes in the room


    # Random chance to find diary
    #IF RANDOM NUMBER BETWEEN 0 AND 1 < 0.3:
        #CALL pick_up("Diary")
        #CALL add_clue("Diary notes hint about compound wings")
    #ELSE:
        #PRINT "You search but find nothing useful"


#DEFINE FUNCTION kitchen():
    #PRINT "You enter the Kitchen"
    #CALL advance_time(30)


    # Random chance for combat or clues
    #IF RANDOM NUMBER BETWEEN 0 AND 1 < 0.4:
        #CALL combat(5)
    #ELSE:
        #CALL add_clue("Strange food scraps… someone was here recently")


#DEFINE FUNCTION hallway():
    #PRINT "You enter the Hallway"
    #CALL advance_time(30)
    #CALL add_clue("Footsteps lead toward the wings")


#DEFINE FUNCTION basement():
    #PRINT "You enter the Basement"
    #CALL advance_time(30)


    # Random chance for combat or item
    #IF RANDOM NUMBER BETWEEN 0 AND 1 < 0.5:
        #CALL combat(8)
    #ELSE:
        #CALL pick_up("Magnifying Glass")


#DEFINE FUNCTION training_room():
    #PRINT "You enter the Training Room"
    #CALL advance_time(30)
    #INCREASE player["strength"] BY 5
    #PRINT "Strength increased!"


#DEFINE FUNCTION puzzle_room():
    #PRINT "You enter the Puzzle Room"
    #CALL advance_time(30)


    # Hard riddle if logic is low
    #IF player["logic"] < 12:
        #PRINT "A tricky riddle confuses you… you waste extra time"
        #CALL advance_time(15)
    #ELSE:
        #CALL add_clue("Puzzle reveals hidden room patterns")


    #INCREASE player["logic"] BY 2
    #PRINT "Logic increased!"


#DEFINE FUNCTION camera_room():
    #PRINT "You found the Camera Room"
    #CALL advance_time(30)
    #CALL add_clue("Camera footage shows the kidnapper pacing in one compound wing")


#DEFINE FUNCTION west_wing():
    #PRINT "Entering West Wing Compound"
    #CALL advance_time(30)


    # Random chance for combat
    #IF RANDOM NUMBER BETWEEN 0 AND 1 < 0.5:
        #CALL combat(10)


    # Check if Emma is here
    #IF emma_room == "West Wing (Compound)":
        #PRINT "EMMA IS HERE! You rescue him!"
        #PRINT "YOU WIN!"
        #EXIT game


    # Check if kidnapper is here
    #IF kidnapper_room == "West Wing (Compound)":
        #CALL add_clue("The kidnapper is hiding in this wing!")


#DEFINE FUNCTION east_wing():
    #PRINT "Entering East Wing Compound"
    #CALL advance_time(30)


    #IF RANDOM NUMBER BETWEEN 0 AND 1 < 0.5:
        #CALL combat(10)


    #IF emma_room == "East Wing (Compound)":
        #PRINT "EMMA IS HERE! You rescue him!"
        #PRINT "YOU WIN!"
        #EXIT game


    #IF kidnapper_room == "East Wing (Compound)":
        #CALL add_clue("The kidnapper is hiding in this wing!")


# Room functions


#CREATE dictionary room_functions mapping:
    #"Library" -> library
    #"Kitchen" -> kitchen
    #"Hallway" -> hallway
    #"Basement" -> basement
    #"Training Room" -> training_room
    #"Puzzle Room" -> puzzle_room
    #"Camera Room" -> camera_room
    #"West Wing (Compound)" -> west_wing
    #"East Wing (Compound)" -> east_wing


# Main Loop


#PRINT "WELCOME TO MYSTERY MANSION!"
#PRINT "Find Emma before 10 PM!"


#WHILE TRUE:
    #CALL show_time()
    #PRINT "Rooms available:"
    #FOR EACH room IN rooms:
        #PRINT room number AND room name


    # Ask player for input
    #GET user input AS choice


    # Validate input
    #IF choice IS NOT A NUMBER:
        #PRINT "Invalid input. Enter a number."
        #CONTINUE to next loop iteration


    # Convert input to index
    #SET selected_room TO rooms[choice - 1]


    #PRINT "Going to selected_room..."
    # Call corresponding room function
    #CALL room_functions[selected_room]()