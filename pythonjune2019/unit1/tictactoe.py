board=["_","_","_",
       "_","_","_",
       "_","_","_"]
currentplayer="X"
game=True
winner=None
def display():
    print(board[0] + " | " + board[1] + " | " + board[2]+ "      1    2    3")
    print(board[3] + " | " + board[4] + " | " + board[5]+ "      4    5    6")
    print(board[6] + " | " + board[7] + " | " + board[8]+ "      7    8    9")


def playgame():
    display()
    while game:
        turn(currentplayer)
        checkgame()
        switch()
    if winner=="X" or winner=="O":
        print(winner+" is winner")
    else:
        print("Its a tie")
def turn(player):
    print(player + "Turn")
    position=input("Enter number from 1-9: ")
    while True:
        if position in ["1","2","3","4","5","6","7","8","9"]:
            position=int(position)-1
            if "_"==board[position]:
                board[position]=player
                display()
                break
            else:
                position = input("Enter number from 1-9: ")
        else:
            position=input("Enter number from 1-9: ")

def switch():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    elif currentplayer=="O":
        currentplayer="X"

def checkgame():
    checkwin()
    checktie()

def checkwin():
    checkrow()
    checkcolumn()
    checkdiag()

def checkrow():
    global game
    global winner
    row1=board[0]==board[1]==board[2]!="_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"

    if row1 or row2 or row3:
        game=False
    if row1:
        winner=board[0]
    elif row2:
        winner=board[3]
    elif row3:
        winner = board[6]

    return winner


def checkcolumn():
    global game
    global winner
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"

    if col1 or col2 or col3:
        game = False
    if col1:
        winner = board[0]
    elif col2:
        winner = board[1]
    elif col3:
        winner = board[2]

    return winner


def checkdiag():
    global winner
    global game
    diag1 = board[0] == board[4] == board[8] != "_"
    diag2 = board[6] == board[4] == board[2] != "_"

    if diag1 or diag2:
        game = False
    if diag1:
        winner = board[0]
    elif diag2:
        winner = board[6]

    return winner

def checktie():
    global game
    if "_" not in board:
        game=False
playgame()