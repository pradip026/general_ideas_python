
# a=int(input('enter value'))
# b=int(input('enter value b'))
#
# print('a is greater than b') if (a>b) else print('b is greater')

li=[1,2,3,4,5,100]
print(sum((li)))
# build in function0 sum iterable


#_doc_string how to use

def function1(a,b):
    """This Function is used to calculate of two numbers"""
    average=(a+b)/2
    return average

p=function1(3,2)
print(p)
print(function1.__doc__)


from array import*
arr1=('i',[2,3,4,1,5,6])
print(arr1)
try:
    print(arr1[6])

except Exception as e:
    print('\n' ,e ,'\n')

print('Try except statement in Python')