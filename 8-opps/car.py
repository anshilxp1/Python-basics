class Car :
    def __init__(self, car_name,color,brand):
        self.car_name= car_name
        self.color    = color
        self.brand    = brand
    def show(self):
        print(f"car_name={self.car_name}")
        print(f"color={self.color}")
        print(f"brand={self.brand}")
#creating a objects

c1= Car( "bmwx", "red" , "BMW")
#c1.show()

c2=Car("audixmp", "black", "AUDI")
print(c2.brand)