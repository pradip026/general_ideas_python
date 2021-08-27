class Student():
    no_of_subject=6
    pass


nam=Student()
add=Student()

nam.name="pradip"
nam.no_of_subject=8

print(nam.__dict__)

add.address='gongabhu'


Student.no_of_subject=7

print(nam.name)
print(add.address)
print(add.no_of_subject)







class Employee():
    no_of_leaves=8

    def printdetails(self):
        return f"Employee name is {self.name},salary is {self.salary} and" \
            f" no of leave is {self.no_of_leaves}"


hari=Employee()
Ram=Employee()

hari.name="Hari"
hari.salary=1234

Ram.name="ram"
Ram.salary=56789

print(hari.printdetails())





class company():
    operation="produce cement"
    working_days="Weekly"

    def __init__(self, no, na, sa, po):
        self.number = no
        self.name = na
        self.salary = sa
        self.post = po



    def printinfo(self):
        return f"Use of Company {self.operation},No of employee in company {self.number}, Name of employee is {self.name}," \
            f" salary is {self.salary} and post is {self.post}"

    @classmethod
    def change(cls,value):
        cls.working_days=value

    @classmethod
    def fromp(cls,string):
        # pra=string.split("-")
        # return cls(pra[0],pra[1],pra[2],pra[3])
        return cls(*string.split("-"))


    @staticmethod
    def printin(sop):
        print("Hello You are using "+sop)




if __name__ == '__main__':
    A_class=company(50, "Hari", 50000, 'labour')
    B_class=company(100, "Ramhari", 5000, 'senior manager')
    C_class=company.fromp("20-harry-4000-manager")
    A_class.change('everyday')
    A_class.printin("Python")
    #print( B_class.working_days())

    print(B_class.printinfo())

    print(A_class.__dict__)
    print(company.__dict__)
    print(C_class.name)
    print( A_class.working_days)
    print( A_class.operation)
