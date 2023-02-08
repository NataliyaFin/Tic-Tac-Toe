# Display game instructions
print("""Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe! 
This will be a showdown between your human brains. 
You will make your move by entering a number of row and col: from 0 to 2. 
The ultimate battle is about to begin! \n """)

# Create a 3x3 board
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

# Initialize player turn and winner
player_turn = 1
winner = None
move_counter = 0

# Create a loop to keep game running
while move_counter < 9:
    # Print board
    for row in board:
        print(row)

    # Ask player for row and col
    if player_turn == 1 and move_counter != 9:
        # Player 1 turn
        print('Player 1 turn')
        row = int(input('Enter row (0 or 1 or 2): '))
        col = int(input('Enter col (0 or 1 or 2): '))
        if row not in range(0, 3) or col not in range(0, 3):
            print("Coordinates should be from 0 to 2!")
        else:
            if board[row][col] != '_':
                print('This cell is occupied! Choose another one!')
            else:
                board[row][col] = 'X'
                move_counter += 1
                player_turn = 2

    elif player_turn == 2 and move_counter != 9:
        # Player 2 turn
        print('Player 2 turn')
        row = int(input('Enter row (0 or 1 or 2): '))
        col = int(input('Enter col (0 or 1 or 2): '))
        if row not in range(0, 3) or col not in range(0, 3):
            print("Coordinates should be from 0 to 2!")
        else:
            if board[row][col] != '_':
                print('This cell is occupied! Choose another one!')
            else:
                board[row][col] = 'O'
                move_counter += 1
                player_turn = 1

    # Check if someone won
    # Check Horizontal
    if board[0][0] == board[0][1] == board[0][2] != '_':
        winner = board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != '_':
        winner = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != '_':
        winner = board[2][0]

    # Check Vertical
    elif board[0][0] == board[1][0] == board[2][0] != '_':
        winner = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != '_':
        winner = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != '_':
        winner = board[0][2]

    # Check Diagonal
    elif board[0][0] == board[1][1] == board[2][2] != '_':
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != '_':
        winner = board[0][2]

# Print board after the game is over
if move_counter == 9:
    for row in board:
        print(row)

# Print winner
if move_counter == 9 and winner is None:
    print('Tie')
else:
    print(f'{winner} won')
