import random


BOARD_SIZE = 5
NUM_SHIPS = 4

# Create the game board
player_board = [['O' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
computer_board = [['O' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Place the battleships at random locations
player_ships = []
computer_ships = []
for _ in range(NUM_SHIPS):
    player_ship_row = random.randint(0, BOARD_SIZE - 1)
    player_ship_col = random.randint(0, BOARD_SIZE - 1)
    player_ships.append((player_ship_row, player_ship_col))
    computer_ship_row = random.randint(0, BOARD_SIZE - 1)
    computer_ship_col = random.randint(0, BOARD_SIZE - 1)
    computer_ships.append((computer_ship_row, computer_ship_col))

# Function to print the game boards
def print_boards(player_board, computer_board):
    print("Player's Board:")
    for row in player_board:
        print(" ".join(row))
    print("\nComputer's Board:")
    for row in computer_board:
        print(" ".join(row))

# Mark the player's battleship locations on their board
for ship_row, ship_col in player_ships:
    player_board[ship_row][ship_col] = '*'

# Game loop
for turn in range(10):  # Ten turns to guess
    print("Turn", turn + 1)
    
    # Print the game boards
    print_boards(player_board, computer_board)
    
    # Ask the player for a guess
    guess_row = int(input("Guess Row (0-4): "))
    guess_col = int(input("Guess Col (0-4): "))
    
    # Check if the guess is correct
    if (guess_row, guess_col) in computer_ships:
        print("Congratulations! You sunk a battleship!")
        computer_board[guess_row][guess_col] = '@'
        computer_ships.remove((guess_row, guess_col))
    elif computer_board[guess_row][guess_col] == 'X':
        print("You guessed that one already.")
    else:
        print("You missed.")
        computer_board[guess_row][guess_col] = 'X'
    
    # Computer's turn
    computer_guess_row = random.randint(0, BOARD_SIZE - 1)
    computer_guess_col = random.randint(0, BOARD_SIZE - 1)
    
    # Check if the computer's guess is correct
    if (computer_guess_row, computer_guess_col) in player_ships:
        print("Oh no! The computer sunk one of your battleships!")
        player_board[computer_guess_row][computer_guess_col] = '@'
        player_ships.remove((computer_guess_row, computer_guess_col))
    else:
        print("The computer missed.")
        player_board[computer_guess_row][computer_guess_col] = 'X'
    
    # Check if all player's ships have been sunk
    if len(player_ships) == 0:
        print("Oh no! The computer sunk all your battleships!")
        break

# Print the final game boards
print("\nFinal Game Boards:")
print_boards(player_board, computer_board)
