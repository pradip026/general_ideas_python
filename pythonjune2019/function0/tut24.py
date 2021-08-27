# dic={'pradip':'1','hari':'2'}
# dic2={(1,'id'),('name',"pradip")}
# print(type(dic))
# print(dic)
#
# for key,value in dic.items():
#     print(key,value)
#
#
#
# value=input('enter value')
# for item in dic:
#     dic1=dic[value]
#
# print(dic1)
#
# dic3={'pradip':'1','hari':'2'}
# dic3['pradip']=2
# print(len(dic3))
# print(dic3)


dict1={}
dict1['name']='Hari'
dict1['address']='Bhaktpur'
dict1['email']=['Hari@gmail.com','Hari12@gmail.com']
dict1['number']=[355546,5462555]

for key,value in dict1.items():
    print(key,"   ",value)

print('name'in dict1)
print(dict1.get('name'))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1.clear())





