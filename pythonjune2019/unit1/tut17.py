#to import function0
# def function0():
#     i=0
#     while(5>i):
#         print('Hello')
#         i=i+1
#
# li=[1,2,3,4,5,6]
# for item in li:
#     print(item)
#
#
# for x in range(1,10):
#     print("Hello world")
#
#
# li2=[True,1,2,'kathmandu',3,'Hello',4,5,6,[1,2,3]]
# for item in li2:
#     if isinstance(item,list):
#
#         for item1 in item:
#             print(item1)
#
#
#     else:
#         print(item)
#

# li2 = [True, 1, 2, 'kathmandu', 3,(5,6,7), 'Hello', [1, 2, 3]]
# for item in li2:
#     if isinstance(item, list)or isinstance(item,tuple):
#          for item1 in item:
#              print(item1)
#
#
#
#     else:
#         print(item)
#
# sum=0
# li=[1,2,3,4,5,6]
# leng=len(li)
# for item in li:
#     sum=sum+item
# average=sum/leng
#
# print(average)
# print(sum)


# for i in range(10,1,-1):
#     print(i)


# list2=list(range(1,10,1))
# print(list2)

# import random
# list4=[]
# for i in range(1,100):
#     list4.append(random.randint(1,100))
#
# print(list4)

# digit=[1,2,3,4]
# for item in digit:
#     print(item)
#
# else:
#     print('No element')

for x in range(1,11):
    if x==5:
        continue
    else:
        print(x)
