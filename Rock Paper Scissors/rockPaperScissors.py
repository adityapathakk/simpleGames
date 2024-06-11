import random
import time

you_score = 0
computer_score = 0
roundWiseWinners = []

def get_user_choice(): # Function to get user's choice (rock, paper, or scissors)
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice(): # Function to randomly generate computer's choice
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice): # Function to determine the winner of the game
    global you_score, computer_score;

    if user_choice == computer_choice:
        roundWiseWinners.append("Tie")
        return "It's a tie!"
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        you_score = you_score + 1
        roundWiseWinners.append("You")
        return "Congratulations! You win this round!"
    
    else:
        computer_score = computer_score + 1
        roundWiseWinners.append("Computer")
        return "Computer wins this round!"



# Function to play the game
print("Let's play Rock, Paper, Scissors!\n")
time.sleep(1.5)
n = int(input("How many rounds do you want to play? "))
m = n
count = 1

while n > 0:
    print(f"\nRound: {count}")
    time.sleep(.75)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    time.sleep(1)
    print(f"Computer chose: {computer_choice}")
    time.sleep(1)
    print(determine_winner(user_choice, computer_choice))
    time.sleep(1)
    count = count + 1
    n = n - 1

if you_score > computer_score:
    print("\nYou won the overall match\n")
elif you_score < computer_score:
    print("\nComputer won the overall match\n")
else:
    print("\nThe match is tied\n")

print("Round-wise Winners:")
for i in range(m):
    print(f"Round {i + 1}: {roundWiseWinners[i]}")
