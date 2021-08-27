def func(a,b,c,d):
     print(a,b,c,d)

func('pradip','samir','hari','ram')



def func1(*arg ):
    print(type(arg))
    for item in arg:
        print(item)



li=[1,2,3,4,5,6]
# func1('pradip','samir','hari','ram')
func1(*li)


def func2(normal,*arg ):

    print(normal)
    for item in arg:
        print(item)

n="This is the list of integer"
li=[1,2,3,4,5,6]
func2(n,'pradip','samir','hari','ram')
# func2(n,*li)





def func3(normal,*arg,**kwargs ):
    print(normal)
    for item in arg:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is a {value}")

n="Use of arguments in python"
li=[1,2,3,4,5,6]
kw={'pradip':'student','samir':'cook','hari':'Rider',
    'ram':'cashier'}
func3(n,*li,**kw)


