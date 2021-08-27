problem=input('Enter a Problem in a word ')
ok=problem.upper()
length=len(ok)
word=list(ok)
li=[]
a=len(li)
game=True
def playhangman():



    for x in range(length):
        print('_' + ' | ', end='')
        a='_'
        li.append(a)
    player1()

def player1():
    global game
    count=0
    global li

    while game:

        if count<=5:
            if '_' in li:
                player=input('\n enter a Letter')
                pl=player.upper()
                if pl=='%':
                    count = count + 1
                    print('Wrong word.....')



                elif pl in word:
                    while pl in word:


                        pos=word.index(pl)
                        word[pos]='%'
                        li[pos]= pl


                    print(li)


                else:
                    count=count+1
                    print('Wrong word.....')
            else:
                print("\nYou are the WINNER")
                game = False
        else:
            print('\nYou are DEAD')
            game=False



playhangman()



