

with open("text1.txt") as f:#no need to close file
    print(f.read())

f=open("text1.txt")
print(f.tell())#find pointer location
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(0)#reverse to original location
print(f.readline())
print(f.read())
f.seek(30)
print(f.readlines())
f.close()
