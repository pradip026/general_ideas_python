i=1
li=[]
def student_info():
    global i,roll,name,clas,se
    roll=int(input('Enter your id:'))
    name=input('Enter your name:')
    clas=int(input('Enter your class'))
    section=input('Enter your section')
    se=section.upper()

    while(i<=4):
        print(f"Enter your marks{i}")
        marks=int(input())

        if marks>100 or marks<0:
            print('\nYou enter wrong mark')
            continue
        else:
            li.append(marks)
            i=i+1


def calc():
    global sum1,average,percent
    sum1=sum((li))
    average=float(sum1/4)
    percent=float(sum1/400)*100
    result()


def result():

        if li[0]<40 or li[1]<40 or li[2]<40 or li[3]<40:
            print('\nYour are failed\n')



        else:
            print('\nCongratulation\n')
            division()


def division():

    if percent < 50 and percent>40:
        print('\nYou are in second division\n')
    elif percent >= 50 and percent < 60:
        print('\nYou are in first Division\n')
    elif percent >= 60 and percent < 80:
        print('\nYou are in First division\n')

    elif percent>80:
        print('\nYou are in Distinction\n')

    else:
        print('\nYour Percent is less than 40--Please attend Re-Exam\n')

def print_section():

    student_info()

    print('student ID is:',roll)
    print('student name is:',name)
    print('Student class is:',clas)
    print('Student section is:',se)

    calc()

    print('Total marks is:',sum1)
    print('Average marks is:',average)
    print('Your Percent is:',percent)


print_section()