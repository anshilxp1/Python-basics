class employee :
    def __init__ (self,name,salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"{self.name},{self.salary}")
class developer(employee) :
    def __init__(self,name ,salary,language):

        #seper() used to call the employee construtor or parent constructor.if we dont call the we have to use 
        #self.name=name
        #self.salary=salary

        super().__init__(salary,name)   
        self.language = language
    def show_language(self):
        print(f"{self.language} language used by developer")     

class manager(employee):
    def __init__(self,name ,salary,team_size):
        super().__init__ (name ,salary)
    def show_team(self):
        print(f"{self.name} manages the team of size {self.show_team}")


d = developer("anshil",50000,"java")
d.show_language()
d.show()
man = manager("aman" , 100000,15)
man.show_team()
man.show




