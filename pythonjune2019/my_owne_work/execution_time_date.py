import datetime
import time
print(datetime.datetime.now())

k=0
initial=time.time()
while(k<10):
    print(k,end='')
    # time.sleep(1)#sleep for 1 sec
    k+=1
print(f"\nExecution time after while loop{time.time()-initial}")
initial1=time.time()
for i in range(10):
    print(i,end='')
print(f"\nExecution time for for loop{time.time()-initial1}")


print(time.asctime())
print(time.asctime(time.localtime(time.time())))


# watch?
# li=[0]
# minute= 0
#
# def second1():
#     while li[0]<60:
#         li[0]+=1
#         time.sleep(1)
#         print(li[0],'sec')
#
#
#     def minute1():
#         global minute
#         minute+=1
#         print(minute,"minute")
#         li[0]=0
#         second1()
#
#     minute1()
# second1()

li=['harry','hari','ram','shyam','ramesh',1,2,3,4]
# i=1
# for item in li:
#     if i%2!=0:
#         print(item)
#     i+=1

for index,item in enumerate(li):
    if index%2!=0:
        print(item)






