def print_hello():
    print("Hello We are working on python")
#
#
#
def print_message(message):
    print(f"{message} is good.")


def get_total():
    num1 = 12
    num2 = 8
    return (num1 + num2)

def do_total(n1,n2):
    return (n1+n2)


def read_int():
    num1=int(input('enter Id value'))
    print("your id Is:",num1)


def read_character():
    st = input('enter section')
    a=st.upper()
    print('your section is:', a)

def read_string():
    name=input('enter your name')
    print('Your name is:',name)


def read_float():
    global mark1, mark2, mark3, mark4, mark5, mark6
    print('enter marks obtained in subject')
    mark1=float(input('marks in english'))
    mark2= float(input('marks in Nepali'))
    mark3= float(input('marks in math'))
    mark4= float(input('marks in science'))
    mark5= float(input('marks in social'))
    mark6= float(input('marks in population'))
def cal():

    sum=mark1+mark2+mark3+mark4+mark5+mark6
    print('total is',sum)

def student_info():
    read_int()
    read_character()
    read_string()
    read_float()
    cal()

if __name__ == '__main__':

    from array import *

    My_array=array('i',[10,20,30,40])
    print(My_array)
    print(type(My_array))
    for item in My_array:
        print(item)
    for i in range(len(My_array)-1,-1,-1):
        print(My_array[i])

