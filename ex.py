print("jaanu"*3)
print("J"+"G")
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
p1=point(1,2)
p2=point(3,4)
print(p1+p2)
class demo:
    def greet(self,*name):
        if name:
            print(f"HELLO,{name}")
        else:
            print("HELLO")
obj=demo()
obj.greet()
obj.greet("jaanu","brunda")
class student:
    def __init__(self,name=None,age=None):
        if name and age:
            print(f"Name:{name},Age:{age}")
        elif name:
            print(f"Name:{name}")
        elif age:
            print(f"Age:{age}")
        else:
            print("No details")
s1=student()
s2=student("Radha")
s3=student("radha",30)
s4=student(age=20)
    
