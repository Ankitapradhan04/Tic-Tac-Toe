global board
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
player = "X"

#print the board in a visually pleasing maner
def printBoard(board):
    for line in board:
        print(line)

#take user input and replace the appropriate space
def makeMove():
    global player
    x = int(input("player " + player + ", What is the X coordinate? "))
    y = int(input("What is the Y coordinate? "))
    
    while board[y][x] != " ":
        print("you must choose an empty spot")
        x = int(input("player " + player + ", What is the X coordinate? "))
        y = int(input("What is the Y coordinate? "))
    
    
    if player == "X":
        board[y][x] = "X"
        player = "O"
    else:
        board[y][x] = "O"
        palayer = "X"


def isWin():
    global player
    #3 in a row
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != player:
                win = False
                break
        if win:
            True
    #3 in a coloumn
    
    #diagonals
    
    return False


def tictac():
    printBoard(board)
    makeMove()
    

def main():
    gamewon = False
    while gamewon == False:
        tictac()
    print("GAMEOVER")
        
        
main()