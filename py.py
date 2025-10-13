class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print("Inside Constructor")
        print("Name:",self.name)
        print("Roll.no:",self.roll_no)
    def update_marks(self,marks):
        self.marks=marks
        print("\nInside Instance method")
        print(f"{self.name}'s Marks updated to",self.marks)
s1=student('Jaanu',101)
print("\n Outside of class")
print("Name(before):",s1.name)
s1.name='Jahnavi'
print("Name(after):",s1.name)
s1.update_marks(90)
print("Marks outside the class:",s1.marks)
