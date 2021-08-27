import random
count=0
def generate():
    global n
    n=random.randint(5,95)
generate()
while True:
    countguess = int(input("Enter: How many LIFE You want"))
    a=countguess
    if countguess<=3 or countguess>6:
        print("Guess must be in between 3 to 7")
        continue

    else:
        break



print(f'                                Remain {countguess}:LIFE')
while countguess>=1:
    count+=1
    num=int(input("Guess The number\n"))
    countguess = countguess - 1
    if(num>n):
        print("YOU enter Greater number Guess less ")
        print(f'                                Remain {countguess}:LIFE')

    elif(num<n):
        print("YOU enter lesser number Guess Greater")
        print(f'                                Remain {countguess}:LIFE')

    elif(num==n):
        print("CONGRATULATION\n")
        print("WINNER WINNER Chicken Dinner")
        print("You Enter correct number in ",count,"times")
        print("DO you Want to play again??")
        print("If Yes press 1")
        play=input()

        if play=='1':
            generate()
            countguess=a
            count=0

        else:
            print("Thanks for Playing")
            break






    if(countguess<=0):
        print("you LOOSE Game\n")
        print(f"The right number is {n}")
        print("DO you Want to play again??")
        print("If Yes press 1")
        play=input()

        if play=='1':
            generate()
            countguess=a
            count=0

        else:
            print("Thanks for Playing")
            break




