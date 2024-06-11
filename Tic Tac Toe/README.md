# pathak's "pyTicTacToe"
### For when you're bored and craving a game of good old Tic Tac Toe in your Terminal :))

Recall how, in our childhood, we played <i>Zero Kaata</i> on the last pages of our notebooks in school.
I created this project out of a desire to revise and work on my Python skills with an amateur yet fun idea. <b>And for the nostalgia</b>.

This was also my submission for what is known as one of the most challenging tasks in <a href = "https://skillsforall.com/course/python-essentials-1?courseLang=en-US&instance_id=da0847b7-e6fc-4597-bc31-38ddd6b07a2e">Cisco Networking Academy's "PCAP-Programming Essentials in Python" course</a>.
The layout of the 'board' was inspired by their prompt for "Project: Tic Tac Toe".

## Background Info.
Instructions given by the course for this game that I implemented by myself are as follows:
<br><br>
<b>Scenario:</b><br>
Your task is to write a simple program which pretends to play tic-tac-toe with the user. We've decided to simplify the game. Here are our assumptions:

1. The computer (i.e., your program) should play the game using 'X's;
2. The user (e.g., you) should play the game using 'O's;
3. The first move belongs to the computer − it always puts its first 'X' in the middle of the board;
4. All the squares are numbered row by row starting with 1 (see the example session below for reference)
5. The user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
6. The program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
7. The computer responds with its move and the check is repeated;
8. Don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

## A few screenshots
Get a feel of the game through these images: (Start -> How it plays out -> If you win :D)

Start :
<br>
<br>
<img width="349" alt="How the game starts" src="https://github.com/adityapathakk/pyTicTacToe/assets/91721440/e95ba557-7c9c-4da8-9096-79046671da8a">
<br>
<br>
How it plays out :
<br>
<br>
<img width="349" alt="How a round (your turn and computer's turn) goes" src="https://github.com/adityapathakk/pyTicTacToe/assets/91721440/d63e5b8d-d11b-4e87-9e81-9231e8101f54">
<br>
<br>
If you win(!) :
<br>
<br>
<img width="349" alt="Screenshot 2023-08-06 at 12 25 34 AM" src="https://github.com/adityapathakk/pyTicTacToe/assets/91721440/66ad72ad-967d-4951-86f0-41b7119c66a7">

## Notes
Yes, there's a little bit of a `Command Line Interface` aesthetic to it, so you can call it basic ¯\\_(ツ)_/¯

I may add some more functionality -
1. Would really like to play with the art of waiting and make the game play out more dramatically, instead of delivering results as soon as you press Enter.
2. Imagine I revamp this using Tkinter and make a full-fledged GUI for this (<b>HAHA THAT'D BE SICK</b>).
