# li=['pradip','pandit','panda']
# print(li)
#
# for item in li:
#     print(item,end=' and ')
#
# a=" is not ".join(li)
# print('\n',a)
#
# from array import *
#
# arr=('str',['pradip','pandit','hero'])
# print(arr)
# for item in arr:
#     print(item)

#
# number=['1','2','3','4']
# for item in number:
#     print(item)
#     item=int(item)
#     item=item+1
#     print(item)
#
# a=list(map(int,number))
# print(a)
# li=[1,2,3]
# # def square(x):
# #     return x*x
# #
# # squ=list(map(square,li ))
#
# squ=list(map(lambda x:x*x,li))
# st=list(map(str,li))
# print(st)
# print(squ)
#
# plus=lambda x,y:x+y
# print(plus(4,4))
#
# def squr(a):
#     return a*a
#
# def cube(a):
#     return a*a*a
#
# lis=[squr,cube]
#
# for i in range(5):
#     val=list(map(lambda x:x(i),lis))
#     print(val)
#
# # ----------------------FILTER____________
# list1=[3,5,1,7,8,9,3]
# def great5(x):
#     return x>5
#
# great=list(filter(great5,list1))
# print(great)


list2=['w',1,2,3,'pradip',6,'hari','r']
def select(x):
    if isinstance(x,int):
        return x


accept=list(filter(select,list2))
print(accept)
print(sum(accept))

for item in accept:
    print(item)

# -----------------------REDUCE--------------------
from functools import reduce

li=[1,2,3,4]
num=reduce(lambda x,y:x+y,li)
print(num)

value=reduce(lambda x,y:x+y,accept)
print(value)

