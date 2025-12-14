# LV 2nd Mystery Game
import random
# GAME SETUP

def create_game_state():
    emma_room = random.choice(["West Wing (Compound)", "East Wing (Compound)"])
    kidnapper_room = "East Wing (Compound)" if emma_room == "West Wing (Compound)" else "West Wing (Compound)"
    
    state = {
        "player": {"strength_health": 100, "logic": 10, "intelligence": 10, "observation": 10},
        "inventory": [],
        "clues_found": [],
        "camera_clue": False,
        "key_stolen": False,
        "diary_misread": False,
        "time_minutes": 8*60,
        "kidnapper_moving": False,
        "game_over": False,
        "emma_room": emma_room,
        "kidnapper_room": kidnapper_room,
        "rooms": ["Library", "Kitchen", "Hallway", "Basement", "Training Room", "Puzzle Room", "Camera Room", "West Wing (Compound)", "East Wing (Compound)"],
        "west_subrooms": ["Storage", "Armory", "Hidden Closet", "Locked Door", "Trap Room", "Fake Passage"],
        "east_subrooms": ["Vent Room", "Secret Office", "Decoy Room", "Locked Door", "Trap Room", "Hidden Chamber"]
    }
    return state

# UTILITY FUNCTIONS
def show_time(time_minutes):
    hours = time_minutes // 60
    mins = time_minutes % 60
    am_pm = "AM" if hours < 12 else "PM"
    display_hour = hours if hours <= 12 else hours - 12
    print(f"Current Time: {display_hour}:{mins:02d} {am_pm}")

def advance_time(minutes, state):
    state["time_minutes"] += minutes
    if state["time_minutes"] >= 21*60 + 45 and not state["kidnapper_moving"]:
        print("The kidnapper has started moving (9:45 PM)!")
        state["kidnapper_moving"] = True
    if state["time_minutes"] >= 22*60:
        print("It is 10 PM! Emma was not rescued in time!")
        state["game_over"] = True
    return state

# COMBAT SYSTEM
def combat(villain_power, state):
    enemy_health = 30 + villain_power * 5
    defending = False

    print("\nCombat starts!")

    while enemy_health > 0 and state["player"]["strength_health"] > 0:
        print("\nCombat Status")
        print(f"Your Health: {state['player']['strength_health']}")
        print(f"Enemy Health: {enemy_health}")

        print("\nChoose your action:")
        print("1. Attack")
        print("2. Defend")
        print("3. Analyze")
        print("4. Run")

        choice = input("> ")

        # PLAYER TURN
        if choice == "1":
            dmg = random.randint(5, 10) + state["player"]["strength_health"] // 20
            enemy_health -= dmg
            print(f"You attack and deal {dmg} damage!")

        elif choice == "2":
            defending = True
            print("You prepare to defend.")

        elif choice == "3":
            state["player"]["intelligence"] += 1
            print("You analyze the enemy. Intelligence increased!")

        elif choice == "4":
            print("You escape the fight!")
            state = advance_time(10, state)
            return state

        else:
            print("Invalid choice.")
            continue

        # CHECK ENEMY DEAD
        if enemy_health <= 0:
            print("You defeated the enemy!")
            state["player"]["strength_health"] += 5
            print("You recover 5 health.")
            return state

        # ENEMY TURN
        enemy_dmg = random.randint(5, 10) + villain_power
        if defending:
            enemy_dmg //= 2
            defending = False
            print("Your defense reduces the damage!")

        state["player"]["strength_health"] -= enemy_dmg
        print(f"The enemy hits you for {enemy_dmg} damage!")

        if state["player"]["strength_health"] <= 0:
            print("You collapsed... Game Over.")
            state["game_over"] = True
            return state

    return state


# CLUES & ITEMS
def pick_up(item, state):
    if item not in state["inventory"]:
        state["inventory"].append(item)
        print(f"You picked up: {item}")
    return state

def add_clue(clue, state):
    if clue not in state["clues_found"]:
        state["clues_found"].append(clue)
        print(f"New clue added: {clue}")
    return state

def reveal_hidden_clue(clue, state):
    if "Magnifying Glass" in state["inventory"] or state["player"]["observation"] >= 12:
        state = add_clue(clue, state)
    else:
        print("You sense something important… but you miss it.")
    return state

def read_diary(state):
    if "Diary" not in state["inventory"]:
        print("You don't have the diary.")
        return state
    if state["player"]["logic"] < 10 or state["player"]["observation"] < 10:
        print("You misread the diary… it gives false directions!")
        state["diary_misread"] = True
        state = add_clue("Diary: Misleading clue placed in wrong wing.", state)
    else:
        print("The diary reveals true hints about the wings.")
        state = add_clue("Diary: True wing avoids traps and decoys.", state)
    return state

def use_master_key(subroom, state):
    if "Master Key" not in state["inventory"]:
        print("You need the Master Key.")
        return False
    if state["key_stolen"]:
        print("The Master Key was stolen earlier!")
        return False
    if state["diary_misread"]:
        print("You use the Master Key… but misleading clues open a decoy!")
        state = advance_time(15, state)
        return False
    print("The Master Key unlocks the door successfully!")
    return True

# ROOM FUNCTIONS
def library(state):
    print("You enter the Library.")
    state = advance_time(30, state)
    if random.random() < 0.4 and "Diary" not in state["inventory"]:
        state = pick_up("Diary", state)
        state = read_diary(state)
    state = reveal_hidden_clue("Early morning dust pattern - wing direction", state)
    return state

def kitchen(state):
    print("You enter the Kitchen.")
    state = advance_time(30, state)
    if random.random() < 0.5:
        state = combat(5, state)
    else:
        state = add_clue("Kitchen crumbs show kidnapper path.", state)
    return state

def hallway(state):
    print("You enter the Hallway.")
    state = advance_time(30, state)
    state = add_clue("Footsteps lead toward a compound wing.", state)
    if state["player"]["observation"] >= 12:
        state = reveal_hidden_clue("Some footsteps are heavier - villain?", state)
    return state

def basement(state):
    print("You enter the Basement.")
    state = advance_time(30, state)
    if random.random() < 0.5:
        state = combat(8, state)
    else:
        state = pick_up("Magnifying Glass", state)
    return state

def training_room(state):
    print("You enter the Training Room.")
    state = advance_time(30, state)

    if "Master Key" not in state["inventory"]:
        state = pick_up("Master Key", state)

    state["player"]["strength_health"] += 10
    print("Strength increased by 10!")
    return state

def puzzle_room(state):
    print("You enter the Puzzle Room.")
    state = advance_time(30, state)
    if state["player"]["logic"] < 12:
        print("The puzzle confuses you… you waste extra time.")
        state = advance_time(20, state)
    else:
        state = add_clue("Puzzle reveals false wings have more traps.", state)
    state["player"]["logic"] += 2
    print("Logic increased!")
    return state

def camera_room(state):
    print("You enter the Camera Room.")
    state = advance_time(30, state)
    state["camera_clue"] = True
    state = add_clue("Camera shows kidnapper was near one wing earlier.", state)
    state["player"]["observation"] += 1
    print("Observation slightly increased from analyzing the footage.")
    return state

# WINGS & SUBROOMS
def handle_subroom(subroom, state, wing):
    if subroom == "Locked Door":
        if use_master_key(state):
            if state["emma_room"] == wing:
                print("You found Emma! You rescue him!")
                state["game_over"] = True
            else:
                print("The room is empty… Emma is not here.")
        return state

    if subroom == "Trap Room":
        print("A trap triggers!")
        trap_dmg = random.randint(5, 15) - (state["player"]["observation"] // 5)
        state["player"]["strength_health"] -= trap_dmg
        print(f"You take {trap_dmg} damage.")
        if state["player"]["strength_health"] <= 0:
            print("You collapsed… Game Over.")
            state["game_over"] = True
        return state
    if subroom in ["Decoy Room", "Fake Passage"]:
        print("This room is a trick!")
        state = add_clue("This wing contains decoys.", state)
        state = advance_time(10, state)
        return state
    if random.random() < 0.3:
        state = combat(7, state)
    state = reveal_hidden_clue("Strange marks hint at correct wing.", state)
    return state

def wing(state, wing_name):
    print(f"Entering {wing_name}.")
    state = advance_time(30, state)

    subrooms = state["west_subrooms"] if "West" in wing_name else state["east_subrooms"]

    while True:
        print("\nChoose a sub-room:")
        for i, room in enumerate(subrooms, 1):
            print(f"{i}. {room}")

        try:
            choice = int(input("Select a sub-room by number: "))
            if 1 <= choice <= len(subrooms):
                chosen_subroom = subrooms[choice - 1]
                break
            else:
                print("Invalid choice.")
        except ValueError:  # Stops game from crashing
            print("Please enter a number:")

    state = handle_subroom(chosen_subroom, state, wing_name)
    return state


def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Please enter yes or no.")


# MAIN GAME LOOP

while True:
    state = create_game_state()

    print("Welcome to Mystery game! You will be a detective who is trying to find Emma, who has been kidnapped and hidden in one of the rooms.")
    print("Emma is a gentleman and a gentle men who is screaming for HELP.")
    print("To find him, you will need to choose a number to move to each room.")
    print("Along the way, you may encounter villains who will try to sabotage you and hurt you so you don't reach Emma.")
    print("During combat, you can choose to Attack, Defend, Analyze, or Run to survive and continue your search.")
    print("The game starts at 8:00 AM but if you don't find Emma before 10PM. He will ...")


    while not state["game_over"]:
        show_time(state["time_minutes"])
        print("\nRooms:")
        for num, room in enumerate(state["rooms"], 1): 
            print(f"{num}. {room}")

        try:
            choice = int(input("Choose a room by number: "))
            if choice < 1 or choice > len(state["rooms"]):
                print("Invalid choice, try again.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        selected_room = state["rooms"][choice - 1]

        if selected_room == "Library":
            state = library(state)
        elif selected_room == "Kitchen":
            state = kitchen(state)
        elif selected_room == "Hallway":
            state = hallway(state)
        elif selected_room == "Basement":
            state = basement(state)
        elif selected_room == "Training Room":
            state = training_room(state)
        elif selected_room == "Puzzle Room":
            state = puzzle_room(state)
        elif selected_room == "Camera Room":
            state = camera_room(state)
        elif selected_room in ["West Wing (Compound)", "East Wing (Compound)"]:
            state = wing(state, selected_room)

    print("Game Over! Thank you for testing Mystery Mansion!")

    if not play_again():
        print("Thanks for playing Mystery Mansion!")
        break