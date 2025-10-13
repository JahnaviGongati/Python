class animal:
    def make_sound(self):
        print("Some generic animal sound.")
class dog(animal):
    def make_sound(self):
        print("Woof!")
class cat(animal):
    def make_sound(self):
        print("Meow!")
class bird(animal):
    def make_sound(self):
        print("Chirp chirp!")
class sushma(animal):
    def make_sound(self):
        print("aaaaaahhhhhhhhhhlodaloadaloada")
animals=[dog(),cat(),bird(),animal(),sushma()]
for animal in animals:
    animal.make_sound()
