class calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.res = 0

    def accept_num(self):
        self.num1 = int(input("enter 1st num :"))
        self.num2 = int(input("enter 2nd num :"))

    def show_result(self):
        print(self.res)

class addition(calculator):
    def add(self):
        self.res = self.num1 + self.res2
class substracrion(calculator):
    def sub(self):
        self.res = self.num1-self.num2
class multiplication(calculator):
    def mul(self):
        self.res = self.num1 * self.num2 
class division(calculator):
    def divide(self):
        self.res = self.num1 / self.num2

obj = division()
obj.accept_num()
obj.divide()
obj.show_result()