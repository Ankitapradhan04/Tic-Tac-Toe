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
        player = "X"


def isWin():
    global player
    if player == "X":
      p = "O"
    else:
      p = "X"
    #3 in a row
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x][y] != p:
                win = False
                break
        if win:
          return True
    #3 in a coloumn
    for c in range(len(board)):
      win = True
      for r in range(len(board)):
        if board[r][c] != p:
          win = False
          break
      if win:
        return True 
    
    #diagonals
    win = True
    for c in range(3):
      if board[c][c] != player:
        win = False
        break
    if win:
      return True
    
    return False


def tictac():
    printBoard(board)
    makeMove()
    

def main():
    gamewon = False
    while gamewon == False:
        tictac()
        gamewon = isWin()
    print("GAMEOVER")
        
        
main()