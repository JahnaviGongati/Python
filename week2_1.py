class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print(f"{self.make} {self.model} is starting.")
    def stop(self):
        print(f"{self.make} {self.model} is stopping.")
my_car = Car("Toyota","Corolla",2020)
my_car.start()
my_car.stop()
