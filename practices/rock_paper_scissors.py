# LV 2nd Rock Paper Scissors
import random

# Keep track of scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    # Exit option
    if user_choice == 'exit':
        print("\nThanks for playing! Final Scores:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Goodbye!")
        break

    # Check for invalid input
    if user_choice not in choices:
        print("Invalid choice. Please try again.\n")
        continue

    # Computer randomly chooses
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Compare choices
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Show current score each round
    print(f"Score → You: {user_score} | Computer: {computer_score}\n")
