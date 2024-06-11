# The 'Secret number' and user guessed number are compared with the following result:
#   If the user guess is greater than or less than 'Secret number' by 10 - the system output is 'Cold'
#   If the user guess is + / - 10 from the 'Secret number' - the system output is 'Hot'
#   If the user guess matches the 'Secret number' - the system prompts 'You guessed it right!!'

import random

def getRandomNumber():
    return random.randrange(1, 100)

def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "Cold"
    elif number == guess:
        return "Right"
    else:
        return "Hot"

def runGuess():
    secretNumber = getRandomNumber()
    while True:
        user_guess = int(input("Enter a number between 1 and 100: "))
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it right!")
            break
        else:
            print(hint)
            
if __name__ == '__main__':
    runGuess()
