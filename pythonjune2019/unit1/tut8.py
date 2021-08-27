list=[["pradip",2],["samir",4],["harry",5],["soel",6],["Rushan",5],["image",5]]
for item,value in list:
    print(item,"has ",value,'pen')

a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))
f=a,b,c
def function(f):
    x,y,z=f

    volume=x*y*z
    return volume

function(f)
print(function(f))
