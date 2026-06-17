class addition:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        sum = self.num1+self.num2 
        return sum
class additionplus(addition):
    def __init__ (self,num1,num2,num3):
        super().__init__(num1,num2)  
        self.num3 = num3

        #method over writing
    def add(self):
        sum = super().add() + self.num3
        return sum



adn = additionplus(10,20,30)

print(adn.add())