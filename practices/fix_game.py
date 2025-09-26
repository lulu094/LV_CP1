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
        if attempts >= max_attempts:
            #Logic Error
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.") 
            game_over = True
        #Type: Logic Error 
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