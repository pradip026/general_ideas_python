# # num1=0
# # num2=0
# # def function1(num1,num2):
# #     """This is Doc string ❤🙌🙌🙌🙌🙌🙌🙌🙌🤔🎉🎉🎉🎉"""
# #     sum=(num1+num2)
# #     return sum
# #
# # print(function1.__doc__)
#
# def add1(func):
#     func()
#     a=2
#     b=3
#     print(a+b)
#
#     def sub1():
#         print(a-b)
#         def mul1():
#             print(a*b)
#
#         mul1()
#
#     return sub1
#
# @add1
# def hem():
#     print("I am doing Mathe mathematical operation")
#
#
# # hem=add1(hem)
# from functools import reduce
#
# def list1(li):
#     print(li)
#     a=reduce(lambda x,y:x+y,li)
#     return a
#
# def check(ab,cd):
#     print(ab)
#     for item in cd:
#         print(item)



def addd(num1,num2=0):
    return(num1+num2)


def swap(a,b):
    a,b=b,a
    return(a,b)

def name1(name="hello",message='hi'):
    print(name+" "+message)


if __name__ == '__main__':

    pass

