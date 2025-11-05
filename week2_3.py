class Animal:
    def make_sound(self):
        print("Some sound")
class Dog(Animal):
    def make_sound(self):
        print("Bark")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
class Bird(Animal):
    def make_sound(self):
        print("Chirp")
animals=[Dog(),Cat(),Bird()]
for animal in animals:
    animal.make_sound()
