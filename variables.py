class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print("Inside Constructor:")
        print("Name:",self.name)
        print("Rollno:",self.roll_no)
    def update_marks(self,marks):
        self.marks=marks
        print("\nInside Instance Method:")
        print(f"{self.name}'s Marks Updated to:",self.marks)
s1=Student("sree",490)
print("\nOutside of class:")
print("Name(before):",s1.name)
s1.name="gnana sree"
print("Name(after):",s1.name)
s1.update_marks(85)
print("Marks(outside):",s1.marks)
