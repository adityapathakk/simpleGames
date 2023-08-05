# Scenario:
    # Your task is to write a simple program which pretends to play tic-tac-toe with the user. We've decided to simplify the game. Here are our assumptions:
    # -> the computer (i.e., your program) should play the game using 'X's;
    # -> the user (e.g., you) should play the game using 'O's;
    # -> the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
    # -> all the squares are numbered row by row starting with 1 (see the example session below for reference)
    # -> the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer,...
    # ... it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
    # -> the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
    # -> the computer responds with its move and the check is repeated;
    # -> don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.


from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    while True:
        try: # we can only accept integer values
            userMove = int(input("Enter your move: "))
        except:
            print("You're only allowed to enter an integer! Please try again.\n")
            continue
        if userMove < 1 or userMove > 9:
            print("Please choose an integer in the range of 1-9.\n")
            continue
        elif str(userMove) not in board[0] and str(userMove) not in board[1] \
        and str(userMove) not in board[2]:
            print("This square is already taken. Try picking another one!\n")
            continue
        
        # whichever valid and free square user selected, we update it with 'O'
        for row in range(3):
            for col in range(3):
                if board[row][col] == str(userMove): # updating if a square is equal to user's choice
                    board[row][col] = 'O'
        
        break # user's move has been accepted, board has been updated

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    
    global freeSquares
    freeSquares = []
    for row in range(3):
            for col in range(3):
                if board[row][col] == 'O' or board[row][col] == 'X': # checking if square is taken
                    continue
                else:
                    freeSquares.append((row,col))
    
    print(freeSquares)

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    if sign == 'O':
        print("Checking to see if you won...")
    else:
        print("Checking to see if the computer won...")
    
    # winning conditions
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        print("No winner.. yet!")

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    while True:
        row = randrange(3)
        col = randrange(3)
        if (row,col) not in freeSquares:
            continue
        else:
            board[row][col] = 'X'
            return


board = [['1','2','3'],['4','X','6'],['7','8','9']]
numOfMoves = 1
# program's first move will always be X in the middle

user, computer = 'O', 'X'
print()
# signs of the player and computer

print("Hi! Welcome to Tic-Tac-Toe.")
print("Sign of the player: 'O' | Sign of the computer: 'X'\n")
print("The computer has made it's first move. Here's the board: ")
display_board(board)
print()

while numOfMoves < 9:
# player's turn

    print("Your turn!\n")
    enter_move(board)
    numOfMoves += 1
    display_board(board)
    print()

    if victory_for(board, user) == True:
        print("Congratulations, you beat the computer! Well played.")
        break
    else:
        print("Currently available squares on the board: ")
        make_list_of_free_fields(board)
        print()

# computer's turn

    print()
    print("It's the computer's turn... ")
    draw_move(board)
    numOfMoves += 1
    display_board(board)
    print()

    if victory_for(board, computer) == True:
        print("Alas, the computer won! Good luck for next time... ")
        break
    else:
        print("Currently available squares on the board: ")
        make_list_of_free_fields(board)
        print()

else:
    print("It's a tie!\n")

print("Thanks for playing! Hope to play again, soon!")