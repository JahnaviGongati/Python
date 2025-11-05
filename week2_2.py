class Animal:
    def speak(self):
        print("Some generic sound")
class Dog(Animal):
    def speak(self):
        print("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
dog=Dog()
cat=Cat()
dog.speak()
cat.speak()
