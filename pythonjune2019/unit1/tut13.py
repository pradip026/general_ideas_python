my_var=None
print(my_var)
print(type(my_var))
print(type(None))
print(id(my_var))
print(id(None))

my_var1=None
print(id(my_var1))

my_var=True
print(type(my_var))
print(id(my_var))

my_var=10
print(id(my_var))

my_var1=10
print(id(my_var1))

my_var1=20
print(id(my_var1))
my_var=30
print(id(my_var))

my_var1,my_var2=40,40
print(id(my_var1))
print(id(my_var2))

my_var=my_var1=my_var2=100
print(id(my_var))
print(id(my_var2))

my_var=300
my_var1=my_var
print(id(my_var))
print(id(my_var1))

# my_var='kathmandu'
#
# del my_var
# print(my_var)


var1=10
var2=10
result=var1==var2
print(result)
#check address
result=var1 is var2
print(result)

result=var1 is not var2
print(result)

result=var1 != var2
print(result)


result=not(var1!=var2)
print(result)

var4=10
var5=10
var6=10
if var4>var5 and var5>var6:
    print(var4)

elif var5>var4 and var4>var6:
    print(var5)
elif var4==var5 or var5==var6:
    print('equal')
else:
    print(var6)



i=0
for i in range(5):
    print('Kathmandu')


li=[1,2,3,4,5]
result=2 in li
print (result)

result1=3 not in li
print(result1)

if 2 in li:
    print('Yes')
import math
import random
num1=int(input('enter value 1'))
num2=int(input('enter value 2'))
add=num1+num2
sq=math.sqrt(num1)
pow=num1**num2
area=num1*num2
a,b=num2,num1
print('sum is',add)
print('square of num 1  is',sq)
print('power is',pow)
print('area  is',area)
print('swap value is',a,b)
for x in range(5):
  print (random.randint(num1,num2))