class test:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
        print("Constructor execution")
    def m1(self):
        print("Student Name:{}\nRollno:{}\nMarks:{}".format(self.name,self.rollno,self.marks))
t1=test("D",1,100)
t2=test(y="A",z=2,x=90)
t3=test("S",3,98)
t1.m1()
t2.m1()
t3.m1()
