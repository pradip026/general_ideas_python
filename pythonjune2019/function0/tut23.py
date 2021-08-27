

def function1(tup):
    li1 = []
    li=list(tup)
    i=0
    for item in li:
       tem=li[i]
       tem+=1
       li1.append(tem)
       i+=1
    tup=tuple(li1)
    return tup


def print1(tup):
    print(tup)