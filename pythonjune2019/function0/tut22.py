# from array import *
# tup1=(20,)
# tup2=2,3,4,5,7
# tup=('sun','mon','tue','wed','thu','fri','sat')
# print(tup2)
# print(type(tup2))
# print(type(tup))
# tup6='sun','mon','tue','wed','thu','fri','sat'
# print(type(tup6))
# list1=[1,2,3,45,6,5]
# arr1=('i',[1,2,3,45,6,5])
# print(arr1)
# tup7=tuple(arr1)
# print(type(tup7))

# print(tup6[0])
#print(tup6[7])#IndexError: tuple index out of range
#print(tup6[-7])#print(tup6[7])#IndexError: tuple index out of range

#
# tup9=(1,'t',True,None,'Hari')
# print(type(tup9))
#
# tup10=([1,2,3],1,array('i',[1,5,6]))
# print(type(tup10))
# print(tup10)
#
# for item in tup10:
#     if isinstance(item,list):
#         for item1 in item:
#             print(item1)
#     elif isinstance(item,array):
#         for item1 in item:
#             print(item1)
#
#     else:
#         print(item)
# print(type(tup10[0]))
# print(type(tup10[2]))
# tup10[0][0]=123
# print(tup10[0])
# tup10[2].append(45)
# print(tup10)
#
# print(tup[:])
# print(tup[:4])
# print(tup[2:5])
# print(tup[:8])
#
# t=(2,1,3)
# tu=(4,5,6)
# tup=t+tu
# print(tup)
# print(min(tup))
# print(max(tup))
# print(sum(tup))
# print(tup.count(3))
# print(tup.index(3))
# print(t==tu)
# print(t!=tu)
# print(t<tu)
# print(t>tu)
# print(3 in tu)
# print(3 not in tu)
# tuu=t
# print(id(tuu))
# print(id(t))
# print(sorted(t))

# tup19=(1,2)*5
# tup19=None
# del tup19#NameError: name 'tup19' is not defined
# print(tup19)

#String Topic


str="Kathmandu"
str1='Kathmandu'
str2="""Kathmandu"""
print(len(str))
print(type(str))
print(isinstance(str,bool))
print(len(str1))
print(type(str1))
print(len(str2))
print(type(str2))
cat=str+str1
print(cat)

print(str[0])

for i in str:
    print(i)

