# num='123'
# num1='123.78'
#
# in2=int(num)
# in1=float(num1)
#
# print(in1+in2)
#
# id=None
# id=int(input('enter'))
# print('your id is:',id)
# print('your id is:'+str(id))
# print(f'you id is:{id}')
# print('your id is:%d'%id)


# var="peraonal details\nname{}\naddress{}"
# print(var.format(' pradip',' gongabhu'))
# a=input('enter 1 num')
# b=input('enter 2 num')
# re=int(a)*int(b)
# vari="Task-1\nenter number{}\nenter second num is{}\nproduct is{}"
#
# print(vari.format(a,b,re))

num=13.89233
print(num)
print('%f'%(num))
print('%.2f'%(num))
print('%0.3f'%(num))
print('%10.4f'%(num))
print('%15.4f'%(num))
print('%15.2f'%(num))

# import math
# print(dir(math))
# print(help(math))
#
# x=6
# if x in range(5):
#     print('pradip')
#
# else:
#     print('Hello')


# value=int(input('enter value'))
# if value>=50 and value<100:
#     print('It is greater than 50')
#
# elif value>=100:
#     print('It is greater than 100')
#
# else:
#     print('It is less than 50 ')
#

# value=int(input('enter value'))
# if value==1:
#     print(str(value)+"= one")
# elif value==2:
#     print(str(value)+"= two")
# elif value == 1:
#     print(str(value) + "= three")
# else:
#     print('other')

# print("Enter a 1 Number a=")
# a=int(input())
# print("Enter a 2 Number b=")
# b=int(input())
# print("Enter a 3 Number c=")
# c=int(input())
# if a>b and b>c:
#     print(str(a)+" is greater")
#
# elif b>a and a>c:
#     print(str(b)+" is greaater")
#
# elif a==b==c:
#     print("A=B=C")
#
# else:
#     print(str(c)+" is greater")


id=int(input('enter id\n'))
name=input('enter name\n')
marks=[]

for x in range(1,7):
    a=int(input('enter marks'+str(x)+'\n'))
    marks.append(a)


sum=marks[0]+marks[1]+marks[2]+marks[3]+marks[4]+marks[5]
percent=float(sum/600)*100

print(str(sum)+'\n')
print(str(percent)+'% \n')

if percent<50:
    print('fail in subject\n')

elif percent>=50 and percent<60:
    print('You are in first Division\n')
elif percent>=60 and percent<80:
    print('You are in First division\n')

else:
    print('You are in Distinction\n')












