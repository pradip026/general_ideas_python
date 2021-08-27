from array import *
# list1=[1, 2, 4, 4, 3, 3, 3, 6, 5]
# list2=['apple','orange','mango','guva']
# list3=['sun','mon','tue','wed','thu','fri','sat']
# list4= ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
#
# print(list1)
# print(list2)
# print(list3)
# print(list4)
#
#
# list1.append(75)
# print(len(list1))
# print(list1.count(75))
#
# print(list1.index(75))
#
# print(list1.count(3))
#
# first_index=list1.index(3)
# print(list1.index(3,first_index+1,len(list1)))
#
# list1.insert(0,123)
# print(list1.count(123))
# print(list1)
#
#
# list5=[1,2,3]
# list1.extend(list5)
# list1=list1+list5
# print(len(list1))
#
# list2.remove('guva')#particular element
# #list2.pop() (remove last element)
# list2.pop(0)#index 0
# print(list2)
#
# list2.clear()
# print(len(list2))
#
# list_1=list1
# list_1[0]=1234
# print(list_1)
# print(id(list_1))
# print(list1)
# print(id(list1))
#
# list_2=list1.copy()
# print(list_2)
# print(id(list_2))
#
# print(list1)
# list1.reverse()
# print(list1)
# list1.sort()#for accending
# print(list1)
# list1.sort(reverse=True)#for descending
# print(list1)

#Task
sum1=0
li=[]
i=1
MAX=int(input('Enter How many value:'))
while i<=MAX:
    print('enter value')
    num=int(input())
    li.append(num)
    i=i+1

print(li)
for item in li:
    sum1=sum1+item
    avg1=sum1/MAX

print(sum1)
print(avg1)

num1=int(input('enter a number to search'))
if num1 in li:
    print('FOUND')
    index1=li.index(num1)
    print(index1)

else:
    print('Not Found')

print('Maximum number is',max(li))
print('Minimum number is',min(li))

li.sort()
print('sorted in Asc',li)
li.reverse()
print('sorted in DESc',li)

arr1=array('i',li)
print(type(arr1))
print(id(arr1))
print(arr1)

list1=list(arr1)
print(list1)

arr1=array('i',list1)
print(type(arr1))
print(id(arr1))
print(arr1)

tup=tuple(arr1)
print(type(tup))
print(tup)

