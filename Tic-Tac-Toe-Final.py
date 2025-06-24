

def printBoard(grid):
    for row in grid:
        print("|", end = "")
        for number in row:
            print(number, end = "|")
        print()  

def checkwinner(current_player, grid):
    for i in range(len(grid)):
        if grid[i][0] == grid[i][1] == grid[i][2] == current_player:
            print(f"Player {current_player} wins!")
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == current_player:
            print(f"Player {current_player} wins diagonally left!")
            return True
    if grid[0][2] == grid[1][1] == grid[2][0] == current_player:
        print(f"Player {current_player} wins diagonally right!")
        return True
    for i in range(len(grid)):
     if grid[0][i] == grid[1][i] == grid[2][i] == current_player:
        print(f"Player {current_player} wins vertically!")
        return True

def switch_player(current_player):
    if current_player == "X":
        return "O"
    if current_player == "O":
        return "X"

player = "X"
player = switch_player(player)

"""
Main functions:
    1) aggregate our program into one header

"""
def main(): 
    board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]] 
    player = "O"
    check = True
    while check == True:
        printBoard(board)
        row = int(input("Enter row where you want to place your piece: "))
        col = int(input("Enter column where you want to place your piece: "))
        board[row][col] = player
        if checkwinner(player,board) == True:
            check = False
        player = switch_player(player)

main()