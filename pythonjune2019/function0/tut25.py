# def outer(num1):
#     def inner(num1):
#         return num1+1
#
#     num2=inner(num1)
#     print(num1,num2)
#
#
# outer(4)
#
#
# def factorial_recursive(n):
#     if n==1:
#         return 1
#
#     else:
#         return(n*factorial_recursive(n-1))
#
#
# print(factorial_recursive(5))
#
# #print(help(str))
# str1=str("Kathmandu,NEPAL")
# str4="N"
# str2=str1.__add__('Nepal')
# print(str2)
# str3=str2.__sizeof__()
# print(str3)
# print(str1.__str__())
#
# print(str1.capitalize())
# a=(str1.casefold())
# b=(str4.casefold())
#
# if a==b:
#     print('True')
# else:
#     print('False')
#
# print(str1.count(str4))
#
#
# print(str1.encode())
#
# print(str1.endswith('NEPAL'))

# print(str1.find('N'))
# li=[]
# str1="what is your name"
# def hello(msg):
#     print(str1.count(msg))
#     i=0
#     while msg in str1:
#
#         if msg in str1:
#             # str1.find(msg)
#             ind=str1.index(msg)
#             i=ind+1
#             li.append(ind)
#             continue
#
# hello("a")
# print(li)
val=input("Enter a character or string you want to Search: ")
val=val.casefold()
li=[]

str1="""This project intends to make a communication and information exchange environment for teachers and students.
This platform will only solely focus on interaction between teacher and students for better learning environment. 
This project will help teachers to find jobs and also helps connecting teachers and students. 
This web platform will enable more interactive teaching and learning environment among the users."""

str1=str1.casefold()
b=len(str1)
def check(msg):
    if msg in str1 and len(msg)>=1:
        start = 0

        for x in range(start,b):

            a=str1.find(msg,start)
            if a==-1:
                break
            li.append(a)
            start = a + 2


    elif msg in str1 and len(msg)==1:
        for index,item in enumerate(str1):
            if item==msg:
                a=index
                li.append(a)
    else:
        print("Not Found")


check(val)
print(li)