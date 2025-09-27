# LV 2nd Debugging
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
         #Type: Run time Error - The bug was a typo in the input prompt string.
         #This bug kept the code from running correctly because the input prompt was not clear.
        guess = int(input("Enter your guess: "))
        attempts += 1
        if attempts >= max_attempts and guess != number_to_guess:
            #Logic Error - without increment, attempts never increse - need to be incremented in the loop
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.") 
            game_over = True
        #Type: Logic Error  - there can only be one if statement but there can be as many elif statements
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        #continue # Logic Error- this makes the code redundant
    print("Game Over. Thanks for playing!")
start_game()