# Faulty calculator
print("enter a first number")
a=int(input())
print("enter a second number")
b=int(input())

print("Enter a operator")
op= input()

if op=="divide" :

            c=float(a/b)
            print("ans =",c)


elif op== "mul" :

            c = float(a * b)
            print("ans =", c)

elif op=="sub" :

            c = float(a - b)
            print("ans =", c)

elif op== "plus" :
            a=int(a)
            b=int(b)

            c = float(a + b)
            print("ans =", c)