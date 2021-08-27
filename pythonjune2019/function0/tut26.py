# val=input("Enter a character or string you want to Search: ")
# val=val.casefold()
# li=[]
#
# str1="""This project intends to make a communication and information
#  exchange environment for teachers and students."""
#
# str1=str1.casefold()
# b=len(str1)
# def check(msg):
#     if msg in str1:
#         start = 0
#
#         for x in range(start,b):
#
#             a=str1.find(msg,start)
#             if a==-1:
#                 break
#             li.append(a)
#             start = a + 2
#
#     else:
#         print("Not Found")
#
#
# check(val)
# print(li)

# st=' 123 '
# str1="Dfghjk123.4"
# res=str1.isalnum()#alphabet and number
# res1=str1.isalpha()#only alphabet
# res4=str1.isascii()
# res5=st.isdecimal()
# res6=st.isdigit()
# res7=str1.islower()
# res8=st.isnumeric()
# res9=st.isprintable()
# res10=str1.isspace()
# res11=str1.istitle()
# print(res11)


# def verification():
#     while True:
#         name = input("Enter your first name")
#         d=name.isalpha()
#
#         le=len(name)
#         if d==True and le>2:
#             print('valid name')
#             break
#
#         else:
#             print('Invalid')
#             continue




# verification()

# st='5452'
# print(st.isupper())
# str1="ghj"
# st=str1.join(st)
# print(st)
#
# st=" dfghjk "
# print(st.lstrip())#remove white space

pa="what is your name"
st=pa.partition(' ')
st1=pa.split(' ')
for item in st1:
    print(item)

r=pa.replace('w','g')
print(r)

