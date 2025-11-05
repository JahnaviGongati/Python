class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("student name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))
s1=Student(x="sree",y=490,z=95)
s1.display()
s2=Student(x="janu",y=491,z=95)
s2.display()
