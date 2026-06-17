class Bank_account:
    def __init__(self,holder,amount):
        self.holder_name = holder
        self.holder_amount = amount

    def show(self):
        print(f" acount holder name:- = {self.holder_name}")
        print(f" acount holder amount:- = {self.holder_amount}")
    def deposite(self,amount):
        if self.holder_amount<= 0:
            print("invalid amount")
            return
        self.holder_amount+= amount
        print(f"{amount} deposited. New balance : {self.holder_amount}")
    def withdraw(self, amount):
        if self.holder_amount <= 0:
            print("invalid amount")
        if amount>self.holder_amount:
            print("insufficient balance")
        else:
            self.holder_amount-= amount
            print(f"{amount} withdrawn. Remaining balance : {self.holder_amount}")

acc1 = Bank_account("ram", 50000)
acc2 = Bank_account("ansh", 10000)
acc3 = Bank_account("harsh",15000)

 #acc2.deposite(5000)
acc1.withdraw(1200)

