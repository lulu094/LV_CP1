# LV 2nd Rock paper scissors
import random
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice == 'exit':
        print("Thanks for playing! Goodbye.")
        break
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")

    elif user_choice == "paper" and computer_choice == "rock":

    elif user_choice == "scissors" and computer_choice == "paper": 

