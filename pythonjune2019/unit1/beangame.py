n=30
li=[1,2,3,4,5,6,7]
game=True
currentplayer='your'


print('DO you want to start game or you want to play first press switch')
while True:
    a=int(input('PRESS:\n1.start\n2.Switch\n'))
    if a==0 or a>=3:
        continue

    else:
        break


def rule():
    print('Game Rule:\n')
    print('1.You can take 1 to 6 beans at a single time\n2.If you take last bean then you will win the game\n')
    print('3.IF you cannot take the last bean you loose\n')
    print('BEST OF LUCK')



def computer():
    global li
    global game
    global n
    while game:
        print('Computer Turn')
        print('remaining ',(n-6))
        n=n-6
        if n==0:
            print('computer Win')
            game=False
            continue

        var=0
        while var<8:
            print('Your Turn')
            var=int(input('Enter number of bean you want to take:\n'))
            var=var
            if var in li:
                print('you take '+str(var)+ ' bean' )
                print('Reamining:',(n-var))
                n=n-var
                break
            else:
                continue



if a==1:
    rule()
    computer()


if a==2:
    rule()
    player()












