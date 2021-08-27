def gettime():
    import datetime
    return datetime.datetime.now()


print("Health management system")
b=int(input("enter 1 for add , 2 for retrive: "))

def add1():
    while True:
        name=input("enter name of person to record: ")
        name=name.lower()
        if name=="":
            break

        e=int(input("add 1 for food or 2 for exercise: "))

        if e==2:
            exer=input("enter your exercise: ")

            with open(name+"-exe.txt","a") as p:
                p.write(str(gettime())+":"+exer+"\n")
                print("Written Succesfully")
        elif e==1:
            food = input("enter name of food you eat: ")

            with open(name+"-food.txt","a") as p:
                p.write(str(gettime())+":"+food+'\n')
                print("Written Succesfully")


        else:
          print("You choose wrong number")
          break

def retrive():
    name=input("enter name whose catalog you want to view ")
    name = name.lower()
    re=int(input("Which one you want to retrive 1 for food 2 for exercise: \n "))
    if re==1:
        with open(name+"-food.txt","r") as p:
            for i in p:
                print(i,end='')


    elif re==2:
        with open(name+"-exe.txt","r") as p:
            print(p.read())




if b == 1:
    add1()


elif b==2:
    retrive()





