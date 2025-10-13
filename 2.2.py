class A:
    def sound(self):
        print("Animal")
class D(A):
    def bark(self):
        print("Dog")
c=D()
c.sound()
c.bark()
