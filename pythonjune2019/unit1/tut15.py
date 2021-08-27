# import random
# li=['p','r','e','w','wa','d','a']
# a=random.choice(li)
# print(a)


# Result processing
# Declare all variables
# accept user input
# prosesssing
# Result

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
def value():
    if percent<50:
        print ('fail in subject\n')

    elif percent>=50 and percent<60:
        print('You are in first Division\n')
    elif percent>=60 and percent<80:
        print('You are in First division\n')

    else:
        print('You are in Distinction\n')

value()


