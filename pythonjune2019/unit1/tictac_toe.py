table=['_','_','_','_','_','_','_','_','_']
currentplayer='x'
game=True
def start():

    print(table[0]+" | "+table[1]+" | "+table[2])
    print(table[3]+ " | "+table[4]+ " | "+ table[5])
    print(table[6]+ " | "+ table[7]+ " | "+ table[8])
def playgame():
    start()

    while game:

        turn(currentplayer)
        switch()
        check()
def switch():
    global currentplayer
    if currentplayer=='x':
        currentplayer='o'

    elif currentplayer=='o':
        currentplayer='x'

def turn(player):
    print(player+"Turn")
    position=int(input('enter position'))
    while True:
        if position<=9 and position>0:
            position=position-1
            if table[position]=='_':
                table[position]=player
                start()

                break
            else:

                position=int(input('Value already entered please enter again'))

        else:
            position=int(input('enter 1 to 9'))



def check():
    checkrow()
    checkcol()
    checkdi()
    checktie()

def checkrow():
    global game
    if table[0]==table[1]==table[2]!='_':
        print('win by',table[0])
        game = False

    elif table[3]==table[4]==table[5]!='_':
        print('win by',table[3])
        game = False

    elif table[6]==table[7]==table[8]!='_':
        print('win by',table[6])
        game = False


def checkcol():
    global game
    if table[0] == table[3] == table[6]!='_':
        print('win by', table[0])
        game=False


    elif table[1] == table[4] == table[7]!='_':
        print('win by', table[1])
        game = False

    elif table[2] == table[5] == table[8]!='_':
        print('win by', table[2])
        game = False

def checkdi():
    global game
    if table[0] == table[4] == table[8]!='_':
        print('win by', table[0])
        game = False

    elif table[2] == table[4] == table[6]!='_':
        print('win by', table[2])
        game = False
def checktie():
    if '_' not in table:
        global game
        print('Game is TIE')
        game=False
playgame()





