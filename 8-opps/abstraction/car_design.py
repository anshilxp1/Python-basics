from abc import abstractmethod,ABC

class vehicale(ABC):
    @abstractmethod
    def engine(self):
        pass

class car(vehicale):

    def engine (self):
        print("all working process of car ...")
class bike(vehicale):
    def engine(self):
        print("all working process of bike....")     

           
    