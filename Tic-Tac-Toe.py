
board = [[".", "X", "."], [".", "X", "."], [".", "X", "."]]  # Initialize a 3x3 board

print(board)
for row in board:
    print("|", end = "")
    for number in row:
        print(number, end = "|")
    print()  # New line after each row

current_player = "X"
for i in range(len(board)):
    if board[i][0] == board[i][1] == board[i][2] == current_player:
        print(f"Player {current_player} wins!")


if board[0][0] == board[1][1] == board[2][2] == current_player:
        print(f"Player {current_player} wins diagonally left!")

if board[0][2] == board[1][1] == board[2][0] == current_player:
        print(f"Player {current_player} wins diagonally right!")

for i in range(len(board)):
     if board[0][i] == board[1][i] == board[2][i] == current_player:
        print(f"Player {current_player} wins vertically!")
#Connect Four Example
