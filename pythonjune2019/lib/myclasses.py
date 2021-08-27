# class ca1():
#     def __init__(self):
#         self.name="pradip"
#         self.lname='pandit'

class calculation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        # self.num3=num1+num2
    # @property
    # def setnumber(self,num1,num2):
    #     self.num1=num1
    #     self.num2=num2
    @property
    def result(self):
        self.num3=self.num1+self.num2
        return self.num3


    def setnum1(self,num1):
        self.num1=num1

    def __str__(self):
        return "Hello"


