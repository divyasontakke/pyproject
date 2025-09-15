import random

def play():
    print("Welcome to Stone-Paper-Scissors!")
    print("Enter your choice: stone, paper, or scissor")
    
    user = input("Your choice: ").lower()
    choices = ["stone", "paper", "scissor"]
    computer = random.choice(choices)
    
    print(f"Computer chose: {computer}")
    
    if user == computer:
        print("It's a tie!")
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        print("You win!")
    elif user in choices:
        print("Computer wins!")
    else:
        print("Invalid input. Please choose stone, paper, or scissor.")

play()
