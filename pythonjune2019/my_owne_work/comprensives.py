ls=[]
num=int(input("Enter the length of list: "))
print("Enter the value in list: ")
for x in range(num):
    v=int(input())
    ls.append(v)

val=input("IN which Form do you want to convert list or dict or set: ")
val=val.lower()
if val=='list':
    li=[item for item in ls]
    print(li)

if val=='dict':
    dic={i:f'item{i}' for i in ls}
    print(dic)
    rev={value:key for key,value in dic.items()}
    print(rev)
if val=='set':
    se={i for i in ls}
    print(se)

if val=='gen':
    generation=(i for i in ls)
    print(generation.__next__())
    print(generation.__next__())
    print(generation.__next__())
    print(generation.__next__())

    # for item in generation:
    #     yield item