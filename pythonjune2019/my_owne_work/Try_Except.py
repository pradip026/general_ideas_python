f=open('text1.txt')
try:
    f=open('text.txt')
    print(f.read())

# except Exception as e:
#     print(e)

except EOFError as e:
    print(e)

except IOError as e:
    print(e)

else:
    print('If exception not run it runs automatically')

finally:
    print("I am Finally and I run in any case")
    f.close()


print('important stuff is running here.....')



li=[1,2,3,4]
def func():
    for item in li:
        print(item)
        # break
        # return item

    else:
        print('For loop is totally run')

a=func()
print(a)

import time

inittime=time.time()
print(inittime)
water=5
while True:
    if time.time()-inittime>water:
        inittime=time.time()
        print('Why')
