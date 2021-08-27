# class company():
#     operation="produce cement"
#     working_days="Weekly"
#
#     def __init__(self, no, na, sa, po):
#         self.number = no
#         self.name = na
#         self.salary = sa
#         self.post = po
#
#
#
#     def printinfo(self):
#         return f"Use of Company {self.operation},No of employee in company {self.number}, Name of employee is {self.name}," \
#             f" salary is {self.salary} and post is {self.post}"
#
#     @classmethod
#     def change(cls,value):
#         cls.working_days=value
#
#     @classmethod
#     def fromp(cls,string):
#         # pra=string.split("-")
#         # return cls(pra[0],pra[1],pra[2],pra[3])
#         return cls(*string.split("-"))
#
#
#     @staticmethod
#     def printin(sop):
#         print("Hello You are using "+sop)
#
#
#
# class programmer(company):
#
#     def printdet(self):
#         return f"Use of Company {self.operation},No of employee in company {self.number}, Name of programmer is {self.name}," \
#             f" salary is {self.salary} and post is {self.post}"
#
#
# if __name__ == '__main__':
#     A_class=company(50, "Hari", 50000, 'labour')
#     B_class=company(100, "Ramhari", 5000, 'senior manager')
#     pra=programmer(100, "Ramhari", 5000, 'senior manager')
#     print(pra.printdet())
#     print(pra.printinfo())
#

    # -----------MULTIPLE INHERITANCE-------------

class Employee():
    def __init__(self,name,address,number):
        self.name=name
        self.address=address
        self.phone=number


    def printinfo(self):
        return f"Employee name is{self.name},address is {self.address}" \
            f" and phone number is {self.phone}"

class player():
    def __init__(self,name,game):
        self.name=name
        self.game=game


    def printdetails(self):
        return f"player name is {self.name},Instrested in {self.game}"

class multipleclass(Employee,player):
    language="python"
    def printdet(self):
        print(f"He is a master of {self.language}")


if __name__ == '__main__':
    name=multipleclass("pradip","gongabhu",34567890)
    pradip=player('hero',["Football"])
    name.printdet()
    print(pradip.printdetails())
    print(name.printinfo())

# ---------------MULTLEVEL INHERITANCE-----------------------------
class ElectronicDevice():
    operate="Electricity"
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price

    def details(self):
        return f"Device name is {self.name} ,model number is {self.model},and price is{self.price}"

class pocket_gadget(ElectronicDevice):
      no_of_device=10

      def __init__(self, name, model, price):
          self.name = name
          self.model = model
          self.price = price



class phone(pocket_gadget):
      no_of_device = 20


pradip=phone('iphone','xs+',140000)
print(pradip.details())
print(pradip.no_of_device)



# public=simple
# protected=_procted
# private=__private
# access them
# print(object._prot)
# print(object._classname__priv)

