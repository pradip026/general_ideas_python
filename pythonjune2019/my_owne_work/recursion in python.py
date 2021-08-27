num=int(input("enter a number"))
def Factorial_iterative(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact


print(Factorial_iterative(num))

def factorial_recursive(n):
    if n==1:
        return 1

    else:
        return(n*factorial_recursive(n-1))


print(factorial_recursive(num))


def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:

        return fibo(n-1)+fibo(n-2)

print(fibo(num))


#lamda function

minus=lambda x,y: x-y
print(minus(9,4))
print(list(map(lambda x:x*x,num)))