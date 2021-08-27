def function1():
    print("i am a good boy")


func2=function1
del function1
func2()



def executor(func):
    func("Hello World")

executor(print)


def dec1(func1):
    def nowexe():
        print("now Executing")
        func1()
        print("executed")

    return nowexe
@dec1
def myname():
    print("I am pradip")

# myname=dec1(myname)
myname()





def add1(fun):
    fun()
    a = 3
    b = 4
    print(a + b)

    def sub1():

        a=3
        b=4
        print(b-a)

        def pro():

            print("product")
        pro()
    return sub1

def start():
    print('Time start')

start=add1(start)
start()



