class Student():

    def __init__(self,id,fname, grade, section, examname):
        self.id = id
        self.fname = fname
        self.grade = grade
        self.section = section
        self.examname = examname

    def details(self):
        return f'Student id is {self.id} name is {self.fname}' \
            f' grade is {self.grade} section is {self.section}' \
            f' and exam name is {self.examname}'



class marks(Student):

    def __init__(self,id,fname,grade,section,examname):
        super().__init__(id,fname,grade,section,examname)
        print("Enter marks obtained")
        self.sub1=int(input('sub1: '))
        self.sub2=int(input('sub2: '))
        self.sub3=int(input('sub3: '))
        self.sub4=int(input('sub4: '))



class totavg(marks):
    def calc(self):
        self.total=self.sub1+self.sub2+self.sub3+self.sub4
        self.avarage=self.total/4


class final(totavg):
    def check(self):
        if self.sub1<40 or self.sub2<40 or self.sub3<40 or self.sub4<40:
            print("You are failed")

        else:
            percent=(self.total/400)*100

            if percent < 50 and percent > 40:
                print('\nYou are in second division\n')
            elif percent >= 50 and percent < 60:
                print('\nYou are in first Division\n')
            elif percent >= 60 and percent < 80:
                print('\nYou are in First division\n')

            elif percent > 80:
                print('\nYou are in Distinction\n')


tol=final(10,'pradip',10,'a','assign')
a=tol.details()
print(a)
tol.check()