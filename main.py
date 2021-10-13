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
    x = int(input(player + ", What is the X coordinate? "))
    y = int(input("What is the Y coordinate? "))
    
    if player == "X":
        board[y][x] = "X"
        player = "O"
    else:
        board[y][x] = "O"
        palayer = "X"
        

def tictac():
    printBoard(board)
    makeMove()
    

def main():
    gamewon = False
    while gamewon == False:
        tictac()
    print("GAMEOVER")
        
        
main()