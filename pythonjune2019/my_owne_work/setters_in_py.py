class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email=f"{self.fname}{self.lname}@gmail.com"

    def printdet(self):
        return f"Employee name is {self.fname} {self.lname}"
    @property
    def email(self):
        return f"{self.fname}{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]

obj=Employee('pradip','pandit')
print(obj.printdet())
print(obj.email)
obj.email="Hello.pandit@gmail.com"

print(obj.fname)
print(obj.email)
print(obj.printdet())