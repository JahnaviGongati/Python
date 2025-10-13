class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start(self):
        print("The",self.make,self.model,self.year,"is starting.")
    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopping.")
car1=car("Hyundai","model1",2022)
car2=car("Kia","model2",2015)
car1.start()
car1.stop()
car2.start()
car2.stop()
              
        
