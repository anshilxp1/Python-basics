class vehicale:
    def __init__ (self,brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} vehicale is driving")
class car(vehicale):
    def drive(self):
        print(f"{self.brand} car is driving")

class bike(vehicale):
    def ride(self):
        print(f"{self.brand} bike is  riding")

c = car("maruti") 
c.start()
c.drive()
b = bike("bullet")
b.start()
b.ride()       
        