class student:
    '''hello'''
print(student.__doc__)
help(student)

class std:
    Name="B"
    roll=111
    Age=18
    def display(self):
        print("Name:",self.Name)
        print("Roll.no:",self.roll)
        print("Age:",self.Age)
s1=std()
s1.display()
s2=std()
s2.Name='A'
s2.roll=122
s2.Age=18
s2.display()
